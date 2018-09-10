from collections import Counter, defaultdict

import pickle
import sys

from xl2py_util import Emitter

class Dependencies(object):
    def __init__(self, picklefilename = None):
        self.dependencies = defaultdict(Counter)

        self.picklefilename = picklefilename
        if picklefilename:
            sys.stderr.write("Unpickling {}\n".format(picklefilename))
            dependencies = pickle.load(open(picklefilename, "rb"))
            if dependencies:
                self.dependencies = dependencies


    def get_add_dependency_fn(self, name):
        dependencies = self.dependencies[name]
        def add_depedency(name, cell_range):
            dependencies[name] += 1
        return add_depedency


    def write_dependencies(self, output_path):
        if not self.picklefilename:
            self.picklefilename = "{}/dependencies.pickle".format(output_path)
            pickle.dump(self.dependencies, open(self.picklefilename, "wb"))

        dotfilename = "{}/dependencies.dot".format(output_path)
        with open(dotfilename, "wt") as dotfile:
            text = self.graphviz_text()
            dotfile.write(text)

        for ws in sorted(self.dependencies.keys()):
            dotfilename = "{}/{}.dot".format(output_path, ws)
            print("Writing {}...".format(dotfilename))

            with open(dotfilename, "wt") as dotfile:
                text = self.graphviz_text_single(ws)
                dotfile.write(text)

            dotfilename = "{}/{}.depndson.dot".format(output_path, ws)
            print("Writing {}...".format(dotfilename))

            with open(dotfilename, "wt") as dotfile:
                text = self.graphviz_text_dependson(ws)
                dotfile.write(text)


    def graphviz_text_single(self, ws):
        done = []
        todo = [ws]

        emitter = Emitter()
        while len(todo):
            ws1 = todo.pop(0)
            done.append(ws1)
            self.emit_node(ws1, emitter)
            for ws2,_ in sorted(self.dependencies[ws1].items()):
                self.emit_edge(ws1, ws2, emitter)
                if ws2 not in done and ws2 not in todo:
                    todo.append(ws2)

        text = emitter.emit
        text = self.wrap_in_graph(text)
        return text

    def graphviz_text_dependson(self, ws):
        done = []
        todo = [ws]

        emitter = Emitter()
        while len(todo):
            ws1 = todo.pop(0)
            done.append(ws1)
            self.emit_node(ws1, emitter)
            for ws2,counts in sorted(self.dependencies.items()):
                if not ws1 in counts:
                    continue

                self.emit_edge(ws2, ws1, emitter)
                if ws2 not in done and ws2 not in todo:
                    todo.append(ws2)

        text = emitter.emit
        text = self.wrap_in_graph(text)
        return text



    def wrap_in_graph(self, text):
        lines = []
        lines.append("digraph dependencies {")
        lines.append("layers=\"one:two:three\";")
        lines.append("outputorder=\"edgesfirst\";")
        lines.append("nodesep=0.75;")
        lines.append(text)
        lines.append("}")
        return "\n".join(lines)



    def emit_node(self, name, emitter):
        shape = "box"
        color = "yellow"

        if name.startswith("Charts_M"):
            shape = "doubleoctagon"
            color = "red2"

        if name.startswith("Charts_D"):
            shape = "octagon"
            color = "orange2"

        if name.startswith("Dashboard"):
            shape = "diamond"
            color = "grey75"

        if name.startswith("Input"):
            shape = "doublecircle"
            color = "limegreen"

        if name.startswith("OLD"):
            shape = "doublecircle"
            color = "grey98"

        attrs = {
            "label": name.replace("_","\\n"),
            "shape": shape,
            "fillcolor": color,
            "style": "filled",
            "fixedsize": "true",
            "width": "2.2",
            "height": "2.2",
            "fontsize": 20,
            "fontname": "Helvetica-Narrow-Bold",
            "penwidth": 2,
            "layer": "two"
        }

        attrs = ["[{}=\"{}\"]".format(k,v) for k,v in attrs.iteritems()]
        attrs = " ".join(attrs)

        emitter.emit = "{} {};".format(name, attrs)

    def emit_edge(self, ws1, ws2, emitter):
        if ws1 == ws2:
            return

        color = "black"
        if ws2.startswith("Charts_M"):
            color = "red2";
            if ws1.startswith("Charts_D"):
                return

        if ws2.startswith("Charts_D"):
            color = "orange2";

        if ws2.startswith("Dashboard"):
            color = "yellow2";

        if ws2.startswith("Input"):
            color = "limegreen";

        attrs = {
            "color": color,
            "arrowhead": "crow",
            "arrowsize": 1.75,
            "penwidth": 3,
            "layer": "one",
            "dir" : "both"
        }

        attrs = ["[{}=\"{}\"]".format(k,v) for k,v in attrs.iteritems()]
        attrs = " ".join(attrs)

        emitter.emit = "{} -> {} {};".format(ws1, ws2, attrs)


    def graphviz_text(self):
        text = Emitter()
        text.indent = 1

        # Nodes
        for name,_ in sorted(self.dependencies.items()):
            self.emit_node(name, text)

        # Edges
        for ws1,counts in sorted(self.dependencies.items()):
            for ws2,_ in counts.items():
                if ws1 != ws2:
                    self.emit_edge(ws1, ws2, text)

        text = self.wrap_in_graph(text.emit)

        return text



if __name__ == "__main__" and len(sys.argv) > 2:
    deps = Dependencies(sys.argv[1])
    deps.write_dependencies(sys.argv[2])
