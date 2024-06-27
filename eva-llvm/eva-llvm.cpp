#include <string>
#include "./src/EvaLLVM.h"

int main(int argc, char const *argv[]){
    std::string program = R"(
    42
    )";
    EvaLLVM eva;
    eva.exec(program);
    return 0;
}