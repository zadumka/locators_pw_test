from playwright.sync_api import sync_playwright, expect

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=500)
    new_context = browser.new_context()
    page = new_context.new_page()
    page.wait_for_load_state("load")
    page.goto("https://victorstashko.github.io/locator_page/?firstname=&lastname=&age=&male=on#")
    page.pause()

    # ! 1 all()
    #for li in page.locator(f'//li').all():
    #    print(li)
    #list_of_li = page.locator(f'//ol/li').all()
    #print(list_of_li)

    # ! 2 all_inner_texts() Повертає масив вузлів. внутрішні текстові значення для всіх відповідних вузлів.

    #list = page.locator(f'//li').all_inner_texts()
    #print(list)
    #list_of_li = page.locator(f'//ol/li').all_inner_texts()
    #print(list_of_li)
    # ? прописати локатор для першого абзацу
    #text = page.locator(f'//p').all_inner_texts()
    #print(text)

    # ! 3 all_text_contents() Повертає масив вузлів. текстові значення вмісту для всіх відповідних вузлів.
    #    texts = page.locator(f'//li').all_text_contents()
    #    print(texts)

    # ! 4 and_() Створює локатор, який відповідає і цьому локатору, і локатору аргументів.
    #    button = page.get_by_role('button').and_(page.get_by_text('click'))
    #    print(button)

    # ! 5 blur() знімає фокус з твого вибраного елемента
    # ! 6 focus() додає фокусування на елемент

    #page.locator(f'//input[@name="lastname"]').focus()
    #page.keyboard.press('L')

    #page.locator(f'//input[@name="lastname"]').blur()
    #page.locator(f'//input[@name="firstname"]').focus()

    # ! 7 bounding_box - я поки ХЗ як його робити

    #box = page.locator(f'//button[text()="submit"]').bounding_box()
    #print(box)
    #page.mouse.click(box["x"] + box["width"] / 2, box["y"] + box["height"] / 2)


    # ! 8 check - дозволяє переконатись чо чекбокс або радіобатон виставлено

    #page.locator(f'//input[@name="male"]').check()


    # ! 9 clear - очищує інпут чи інше поле для вводу

#    page.locator(f'//input[@name="firstname"]').fill('Test')
#    page.locator(f'//input[@name="firstname"]').clear()


# ! 10 click -

page.locator(f'//button[@class = "btn-primary"]').click()
page.wait_for_timeout(2000)

