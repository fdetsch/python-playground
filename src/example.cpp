#include <pybind11/pybind11.h>
#include <pybind11/stl.h>

namespace py = pybind11;

int add(int i, int j) {
    return i + j;
}

using namespace std;

// 1-dimensional vector
std::vector<double>  vec1d(double a, double b) {
    std::vector<double> out = {a, b * 2};
    return out;
}

// // explicit type conversion, see https://stackoverflow.com/a/54830064
// py::list vec1d(double a, double b) {
//     std::vector<double> out = {a, b * 2};
//     py::list lst = py::cast(out);
//     return lst;
// }

// 2-dimensional vector
std::vector<std::vector<int>> vec2d(int nrow, int ncol) {
    std::vector<std::vector<int>> out(nrow, std::vector<int>(ncol, 0));
    return out;
}

PYBIND11_MODULE(example, m) {
    m.doc() = "pybind11 example plugin"; // optional module docstring
    
    m.def("add", &add, "A function which adds two numbers",
          py::arg("i") = 1, py::arg("j") = 2);
    
    m.def("vec1d", &vec1d, "A function which returns a 1-d vector as list",
          py::arg("a") = 1., py::arg("b") = 2.5);
    
    m.def("vec2d", &vec2d, "A function which returns a 2-d vector as list",
          py::arg("nrow") = 2, py::arg("ncol") = 3);
}
