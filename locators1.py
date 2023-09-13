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

    # ? 7 bounding_box - я поки ХЗ як його робити

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

    # ! 15 evaluate - оцінити. Виконайте код JavaScript на сторінці, взявши відповідний елемент як аргумент.

    # ! 16 get_by_role - Позволяет находить элементы по их роли ARIA, атрибутам ARIA и доступному имени.
    #    expect(page.get_by_role("heading", name="Helloo")).to_be_visible()
    #    page.get_by_role("checkbox", name="female").check()
    #    page.get_by_role("button", name="submit").click()

    # ! 17 get_by_test_id Найдите элемент по идентификатору теста.

    #    page.get_by_test_id("directions").click()

    # ! 18 get_by_text - Позволяет находить элементы, содержащие заданный текст.

    #print(page.get_by_text("Text1"))


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

    #locator = page.frame_locator(f'//div[@class= "iframe"]').get_by_text("Посмотреть")
    #locator.click()


    # ! 24 highlight - Выделите соответствующий элемент(ы) на экране.
    # ! Полезно для отладки, не фиксируйте код, который использует

    #element = page.locator(f'//button[@class = "btn-primary"]')
    #element.highlight()
    #page.wait_for_timeout(2000)

    # ! 25 hover - Наведите курсор на соответствующий элемент.

    #page.get_by_test_id("directions").hover()

    # ! 26 fill -
    #page.locator(f'//input[@name="firstname"]').fill('Test')

    # ! 27 filter- Цей метод звужує наявний локатор відповідно до параметрів,
    # !наприклад, фільтрує за текстом. Його можна багаторазово фільтрувати.

    #row_locator = page.locator(f'//div[@class = "btns"]')
    # ...
    #row_locator.filter(has_text="submit").filter(
    #    has=page.get_by_role("button", name="submit")
    #).screenshot()

    # ! 28 focus

    # page.locator(f'//input[@name="age"]').focus()

    # ! 29 inner_html -
    #ul_list = page.locator(f'//ul')
    #print(ul_list.inner_html())

    # ! 30 inner_text

    #text = page.locator(f'//p')
    #print(text.inner_text())

    # ! 31 input_value - Повертає значення для відповідного елемента <input>, <textarea> або <select>.

    #page.locator(f'//input[@name= "firstname"]').fill("test")
    #check_input = page.locator(f'//input[@name= "firstname"]').input_value()
    #print(check_input)

    # ! 32 is_checked - Повертає, чи перевірено елемент.
    # ! Викидає, якщо елемент не є прапорцем або радіобатоном.

    #print(page.locator(f'//input[@id= "male"]').is_checked())
    #print(page.locator(f'//input[@name= "idk"]').is_checked())

    # ! 33 is_disabled - Повертає, чи елемент вимкнено, протилежно включеному.

    #print(page.locator(f'//button[@name="submit"]').is_disabled())
    #print(page.locator(f'//button[@class="btn-disable"]').is_disabled())


    # ! 34 is_editable - Повертає, чи можна редагувати елемент.

    #print(page.locator(f'//input[@name= "firstname"]').is_editable())
    #print(page.locator(f'//ul').is_editable())
    # ? який локатор не підставиш завжди виводе тру

    # ! 35 is_enabled - Повертає, чи ввімкнено елемент.

    #print(page.locator(f'//button[@name="submit"]').is_enabled())
    #print(page.locator(f'//button[@class="btn-disable"]').is_enabled())

    # ! 36 is_hidden - Повертає, чи є елемент прихованим або видимим.

    #print(page.get_by_alt_text('nature1').is_hidden())
    #print(page.get_by_alt_text('ball').is_hidden())
    #print(page.locator(f'//img[@class="hidden"]').is_hidden())

    # ! 37 is_visible - Повертає, чи є елемент видимим.
    #print(page.get_by_alt_text('ball').is_visible())
    #print(page.locator(f'//img[@class="hidden"]').is_visible())

    # ! 38 locator - Метод знаходить елемент, який відповідає вказаному селектором у піддереві локатора.
    # ! Він також приймає параметри фільтра, подібні до методу locator.filter().

    #locator = page.get_by_role("button", name="submit")
    #locator.hover()
    #locator.click()

    # ? 39 nth - Повертає локатор до n-го відповідного елемента. Він заснований на нулі, nth(0) вибирає перший елемент.
    # ? 40 or_ Створює локатор, який відповідає будь-якому з двох локаторів
    # ? 41 press - Фокусує відповідний елемент і натискає комбінацію клавіш.
    # ? 42 screenshot - Зробіть скріншот елемента, який відповідає локатору
    # ? 43 scroll_into_view_if_needed - Цей метод очікує на перевірку функціональності, а потім намагається прокрутити елемент у поле зору,
    # ?якщо він не повністю видимий, як визначено коефіцієнтом IntersectionObserver.
    # ? 44 select_option Вибирає параметр або параметри в <select>.
    # ? 45 select_text - Цей метод очікує перевірки функціональності, потім фокусує елемент і вибирає весь його текстовий вміст.
    # ? 46 set_checked - Встановити стан прапорця або радіоелемента
    # ? 47 set_input_files - Завантажте файл або декілька файлів у <input type=file>.
    # ? 48 tap - Виконайте жест торкання елемента, який відповідає локатору
    # ? 49 text_content - Returns the node.textContent.
    # ? 50 type - Фокусує елемент, а потім надсилає події натискання клавіші,
    # ? натискання/введення та натискання клавіші для кожного символу в тексті.
    # ? 51 uncheck - Переконайтеся, що прапорець або перемикач знято.
    # ? 52 wait_for - Повертає, якщо елемент, указаний локатором, задовольняє параметр стану.
    # ? 53 first - Returns locator to the first matching element.
    # ? 54 last - Returns locator to the last matching element.
    # ? 55 page - Сторінка, якій належить цей локатор.
    # ? 56 element_handle - Розв’язує заданий локатор до першого відповідного елемента DOM.
    # ? Якщо відповідних елементів немає, очікується на один. Якщо декілька елементів відповідають локатору, кидає.
    # ? 57 element_handles - Розв’язує заданий локатор для всіх відповідних елементів DOM.
    # ? Якщо відповідних елементів немає, повертає порожній список.












