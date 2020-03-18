#include <iostream>
#include <thread>

void shit()
{
}

int main()
{
    std::thread t(shit);

    std::cout << std::thread::hardware_concurrency() << std::endl;

    std::cout << t.get_id() << std::endl;

    std::cout << std::this_thread::get_id() << std::endl;

    t.join();

    return 0;
}
