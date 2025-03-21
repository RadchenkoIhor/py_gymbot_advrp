import asyncio
import keyboard
import threading
import time

print("\n Бот для автоматичної прокачки сили в спортзалі на Advance RP\n")
print(" Для активації / деактивації - використовуйте клавішу Delete \n")

active = False

def listen_keys():
    def on_press(keyboard_event):
        global active
        if keyboard_event.name == 'delete':
            if not hasattr(listen_keys, "last_toggle_time"):
                listen_keys.last_toggle_time = 0
            current_time = time.time()

            if current_time - listen_keys.last_toggle_time > 1:
                active = not active
                if active:
                    print(" ACTIVATED\n")
                else:
                    print(" DEACTIVATED\n")
                listen_keys.last_toggle_time = current_time
    keyboard.hook(on_press)

async def autopress():
    while True:
        if active:
            keyboard.press("h")
            await asyncio.sleep(5)
            keyboard.release("h")
            await asyncio.sleep(4)
        else:
            await asyncio.sleep(0.1)

def run_async_tasks():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(autopress())


if __name__ == "__main__":
    thread1 = threading.Thread(target=listen_keys)
    thread2 = threading.Thread(target=run_async_tasks)
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()