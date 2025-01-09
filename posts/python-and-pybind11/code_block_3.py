#include <pybind11/pybind11.h>
#include <vector>

namespace py = pybind11;

std::vector<double> square_vector(const std::vector<double>& vec) {
  std::vector<double> result;
  for (double x : vec) {
    result.push_back(x * x);
  }
  return result;
}

PYBIND11_MODULE(advanced_example, m) {
  m.doc() = "Advanced pybind11 example plugin";
  m.def("square_vector", &square_vector, "Squares each element in a vector");
}