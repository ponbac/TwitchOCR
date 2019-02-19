import vision
import screenshot
import time

unique_messages = set()
old_messages = list()
new_messages = list()

api_calls = 0

while True:
    text = vision.detect_text(screenshot.take_screenshot())
    api_calls += 1

    print('\n\n\n\n\n\n\n\n\n\n\n')
    print('API CALLS: ' + str(api_calls))

    old_messages = list.copy(new_messages)
    new_messages.clear()

    for l in str.splitlines(text):
        if ':' in l[8:] and '-' not in l and "'" not in l and 'Eye of the Herald' not in l and '!' not in l\
                and 'Kill Reward' not in l:
            new_messages.append(l)

    for m in new_messages:
        if m in old_messages:
            unique_messages.add(m)

    for m in unique_messages:
        print(m)

    time.sleep(5)
