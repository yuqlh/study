#include <iostream>
#include <thread>
#include <chrono>
#include <future>

void print(std::future<int> &f)
{
    std::cout << "what a big shit!" << std::endl;
    int x = f.get();
    std::cout << x << std::endl;
}

int main()
{
    std::promise<int> p;
    std::future<int> f = p.get_future();
    std::thread t(print, std::ref(f));

    std::this_thread::sleep_for(std::chrono::seconds(3));
    p.set_value(100);
    t.join();

    return 0;
}
