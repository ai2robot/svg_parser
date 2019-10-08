# coding=UTF-8
import sys
import xml.etree.ElementTree as ET

#svg支持的图形：矩形，圆形，椭圆，直线，曲线，多边形，路径
svg_shapes = set(['rect', 'circle', 'ellipse', 'line', 'polyline', 'polygon', 'path'])


class Rect:
    def __init__(self, xml_node):
        self.xml_node = xml_node

        if self.xml_node is not None:
            rect_el = self.xml_node
            self.x = float(rect_el.get('x')) if rect_el.get('x') else 0
            self.y = float(rect_el.get('y')) if rect_el.get('y') else 0
            self.rx = float(rect_el.get('rx')) if rect_el.get('rx') else 0
            self.ry = float(rect_el.get('ry')) if rect_el.get('ry') else 0
            self.width = float(rect_el.get('width')) if rect_el.get('width') else 0
            self.height = float(rect_el.get('height')) if rect_el.get('height') else 0
            print("Rect: x=%f, y=%f, rx=%f, ry=%f, width=%f, height=%f"
                  % (self.x, self.y, self.rx, self.ry, self.width, self.height))
        else:
            self.x = self.y = self.rx = self.ry = self.width = self.height = 0
            print("Rect: Unable to get the attributes for %s", self.xml_node)


class Circle:
    def __init__(self, xml_node):
        self.xml_node = xml_node

        if self.xml_node is not None:
            circle_el = self.xml_node
            self.cx = float(circle_el.get('cx')) if circle_el.get('cx') else 0
            self.cy = float(circle_el.get('cy')) if circle_el.get('cy') else 0
            self.rx = float(circle_el.get('r')) if circle_el.get('r') else 0
            self.ry = self.rx
            print("Circle: cx=%f, cy=%f, rx=%f, ry=%f"
                  % (self.cx, self.cy, self.rx, self.ry))
        else:
            self.cx = self.cy = self.r = 0
            print("Circle: Unable to get the attributes for %s", self.xml_node)


class Ellipse:
    def __init__(self, xml_node):
        self.xml_node = xml_node

        if self.xml_node is not None:
            ellipse_el = self.xml_node
            self.cx = float(ellipse_el.get('cx')) if ellipse_el.get('cx') else 0
            self.cy = float(ellipse_el.get('cy')) if ellipse_el.get('cy') else 0
            self.rx = float(ellipse_el.get('rx')) if ellipse_el.get('rx') else 0
            self.ry = float(ellipse_el.get('ry')) if ellipse_el.get('ry') else 0
            print("Ellipse: cx=%f, cy=%f, rx=%f, ry=%f"
                  % (self.cx, self.cy, self.rx, self.ry))
        else:
            self.cx = self.cy = self.rx = self.ry = 0
            print("Ellipse: Unable to get the attributes for %s", self.xml_node)


class Line:
    def __init__(self, xml_node):
        self.xml_node = xml_node

        if self.xml_node is not None:
            line_el = self.xml_node
            self.x1 = float(line_el.get('x1')) if line_el.get('x1') else 0
            self.y1 = float(line_el.get('y1')) if line_el.get('y1') else 0
            self.x2 = float(line_el.get('x2')) if line_el.get('x2') else 0
            self.y2 = float(line_el.get('y2')) if line_el.get('y2') else 0
            print("Line: x1=%f, y1=%f, x2=%f, y2=%f"
                  % (self.x1, self.y1, self.x2, self.y2))
        else:
            self.x1 = self.y1 = self.x2 = self.y2 = 0
            print("Line: Unable to get the attributes for %s", self.xml_node)


class Polyline:
    def __init__(self, xml_node):
        self.xml_node = xml_node
        self.points = list()

        if self.xml_node is not None:
            polyline_el = self.xml_node
            points = polyline_el.get('points') if polyline_el.get('points') else list()
            for point in points.split():
                self.points.append(point)
                print point
        else:
            print("Polyline: Unable to get the attributes for %s", self.xml_node)


class Polygon:
    def __init__(self, xml_node):
        self.xml_node = xml_node
        self.points = list()

        if self.xml_node is not None:
            polygon_el = self.xml_node
            points = polygon_el.get('points') if polygon_el.get('points') else list()
            for point in points.split():
                self.points.append(point)
                print point
        else:
            print("Polygon: Unable to get the attributes for %s", self.xml_node)


class Path:
    def __init__(self, xml_node):
        self.xml_node = xml_node

        if self.xml_node is not None:
            path_el = self.xml_node
            self.d = path_el.get('d')
            print self.d
        else:
            self.d = None
            print("Path: Unable to get the attributes for %s", self.xml_node)


def parser(svg_file):
    tree = ET.parse(svg_file)
    root = tree.getroot()

    width = root.get('width')
    height = root.get('height')

    if len(width) == 0 or len(height) == 0:
        print "width or height is 0"
        exit(1)

    if "mm" in width:
        width = width[:-2]

    if "mm" in height:
        height = height[:-2]

    print width, height

    for elem in root.iter():
        try:
            _, tag_suffix = elem.tag.split('}')
        except ValueError:
            continue

        if tag_suffix in svg_shapes:
            tag_suffix = tag_suffix.capitalize()
            print tag_suffix
            shape_class = globals()[tag_suffix](elem)


