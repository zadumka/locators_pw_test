from playwright.sync_api import sync_playwright, expect

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=500)
    new_context = browser.new_context()
    page = new_context.new_page()
    page.wait_for_load_state("load")
    page.goto("https://victorstashko.github.io/locator_page/?firstname=&lastname=&age=&male=on#")
    page.pause()

    # ! 1 all()
    # for li in page.locator(f'//li').all():
    #    print(li)
    # list_of_li = page.locator(f'//ol/li').all()
    # print(list_of_li)

    # ! 2 all_inner_texts() Повертає масив вузлів. внутрішні текстові значення для всіх відповідних вузлів.

    # list = page.locator(f'//li').all_inner_texts()
    # print(list)
    # list_of_li = page.locator(f'//ol/li').all_inner_texts()
    # print(list_of_li)
    # ? прописати локатор для першого абзацу
    # text = page.locator(f'//p').all_inner_texts()
    # print(text)

    # ! 3 all_text_contents() Повертає масив вузлів. текстові значення вмісту для всіх відповідних вузлів.
    #    texts = page.locator(f'//li').all_text_contents()
    #    print(texts)

    # ! 4 and_() Створює локатор, який відповідає і цьому локатору, і локатору аргументів.
    #    button = page.get_by_role('button').and_(page.get_by_text('click'))
    #    print(button)

    # ! 5 blur() знімає фокус з твого вибраного елемента
    # ! 6 focus() додає фокусування на елемент

    # page.locator(f'//input[@name="lastname"]').focus()
    # page.keyboard.press('L')

    # page.locator(f'//input[@name="lastname"]').blur()
    # page.locator(f'//input[@name="firstname"]').focus()

    # ! 7 bounding_box - я поки ХЗ як його робити

    # box = page.locator(f'//button[text()="submit"]').bounding_box()
    # print(box)
    # page.mouse.click(box["x"] + box["width"] / 2, box["y"] + box["height"] / 2)

    # ! 8 check - дозволяє переконатись чо чекбокс або радіобатон виставлено

    # page.locator(f'//input[@name="male"]').check()

    # ! 9 clear - очищує інпут чи інше поле для вводу

    #    page.locator(f'//input[@name="firstname"]').fill('Test')
    #    page.locator(f'//input[@name="firstname"]').clear()

    # ! 10 click -

    #    page.locator(f'//button[@class = "btn-primary"]').click()

    # ! 11 count - Повертає кількість елементів, які відповідають локатору.

    #    count = page.locator(f'//ol/li').count()
    #    print(count)

    # ! 12 dblclick - подвійний клік, або можна використовувати для проставлення і зняття галочки в чекбоксах

    #    page.locator(f'//input[@name = "idk"]').dblclick()

    # ! 13 dispatch_event - Програмно надішліть подію для відповідного елемента.

    #    page.locator(f'//button[@class = "btn-primary"]').dispatch_event('click')

    # ! 14 drag_to - Перетягніть вихідний елемент до цільового елемента та відпустіть його.

    #    source = page.locator(f'//div[@class = "image"]/img')
    #    target = page.locator(f'//div[@class = "block"]')
    #    source.drag_to(target)
    #    print('drag image')

    # ! 15 evaluate - оцінити

    # ! 16 get_by_role - Позволяет находить элементы по их роли ARIA, атрибутам ARIA и доступному имени.
    #    expect(page.get_by_role("heading", name="Helloo")).to_be_visible()
    #    page.get_by_role("checkbox", name="female").check()
    #    page.get_by_role("button", name="submit").click()

    # ! 17 get_by_test_id Найдите элемент по идентификатору теста.

    #    page.get_by_test_id("directions").click()

    # ? 18 get_by_text - Позволяет находить элементы, содержащие заданный текст.

    #    print(page.get_by_text("first"))

    # ! 19 get_by_title - Позволяет находить элементы по их атрибуту заголовка.

    #expect(page.get_by_title("second_li")).to_be_visible()

    # ! 20 get_by_placeholder - Позволяет находить элементы ввода по тексту-заполнителю.

    #page.get_by_placeholder("type a firstname").fill("Alyona")

    # ! 21 get_by_label - Позволяет находить элементы ввода по тексту связанного элемента
    # ! <label> или aria-labeledby или по атрибуту aria-label.

    #page.get_by_label("firstname").fill("john")

    # ! 22 get_by_alt_text - Позволяет находить элементы по их альтернативному тексту.

    #page.get_by_alt_text("ball").click()

    # ! 23 get_attribute - Возвращает значение атрибута соответствующего элемента.

    #img_w = page.get_by_alt_text("ball").get_attribute("width")
    #print(img_w)

    # ? 24 frame_locator - При работе с iframe вы можете создать локатор фрейма,
    # ! который будет входить в iframe и позволять находить элементы в этом iframe:

    #locator = page.frame_locator("YouTube video player").get_by_text("Смотреть")


    # ! 24 highlight - Выделите соответствующий элемент(ы) на экране.
    # ! Полезно для отладки, не фиксируйте код, который использует

    #element = page.locator(f'//button[@class = "btn-primary"]')
    #element.highlight()
    #page.wait_for_timeout(2000)

    # ! 25 hover - Наведите курсор на соответствующий элемент.

    #page.get_by_test_id("directions").hover()





