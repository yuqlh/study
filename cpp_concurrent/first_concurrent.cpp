#include <iostream>
#include <thread>

void shit()
{
    std::cout << "what a big shit!" << std::endl;
}

int main()
{
    std::thread t(shit);

    t.join();

    return 0;
}
