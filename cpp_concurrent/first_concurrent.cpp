#include <iostream>
#include <thread>

void shit()
{
    std::cout << "what a big shit!" << endl;
}

int main()
{
    std::thread t(shit);

    return 0;
}
