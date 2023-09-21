from playwright.sync_api import sync_playwright, expect
from tornado.web import url

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=500)
    new_context = browser.new_context()
    page = new_context.new_page()
    page.wait_for_load_state("load")
    page.goto("https://victorstashko.github.io/locator_page/?firstname=&lastname=&age=&male=on#")
    #page.goto("https://zadumka.github.io/goit-hw-06/")
    page.pause()


    # ! 1 all() - повертає масив локаторів, які вказують на відповідні елементи
    # for li in page.locator(f'//li').all():
    #    print(li)
    # list_all_li = page.locator(f'//ol/li').all()
    # print(list_all_li)

    # ! 2 all_inner_texts() Повертає масив вузлів. внутрішні текстові значення для всіх відповідних вузлів.

    # list = page.locator(f'//li').all_inner_texts()
    # print(list)
    # list_of_li = page.locator(f'//ol/li').all_inner_texts()
    # print(list_of_li)
    # # ? прописати локатор для першого абзацу
    # text = page.locator(f'//p').all_inner_texts()
    # print(text)

    # ! 3 all_text_contents() Повертає масив вузлів. текстові значення вмісту для всіх відповідних вузлів.
    # texts = page.locator(f'//li').all_text_contents()
    # print(texts)

    # ! 4 and_() Створює локатор, який відповідає і цьому локатору, і локатору аргументів.
    # button = page.get_by_role('button').and_(page.get_by_text('click'))
    # print(button)

    # ! 5 blur() знімає фокус з твого вибраного елемента
    # ! 6 focus() додає фокусування на елемент

    # page.locator(f'//input[@name="lastname"]').focus()
    # page.keyboard.press('L')
    #
    # page.locator(f'//input[@name="lastname"]').blur()
    # page.locator(f'//input[@name="firstname"]').focus()

    # ! 7 bounding_box - Этот метод возвращает ограничивающую рамку элемента, соответствующую локатору

    # box = page.get_by_role("button", name="submit").bounding_box()
    # print(box)
    # page.mouse.click(box['x'] + box['width'] / 2, box['y'] + box['height'] / 2)

    # ! 8 check - дозволяє переконатись що чекбокс або радіобатон виставлено

    # page.locator(f'//input[@name="male"]').check()

    # ! 9 clear - очищує інпут чи інше поле для вводу

    #    page.locator(f'//input[@name="firstname"]').fill('Test')
    #    page.locator(f'//input[@name="firstname"]').clear()

    # ! 10 click - натискає на елемент

    #    page.locator(f'//button[@class = "btn-primary"]').click()

    # ! 11 count - Повертає кількість елементів, які відповідають локатору.

    # count = page.locator(f'//ol/li').count()
    # print(count)

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
    # title_locator = page.locator("h1")  # Знаходимо заголовок сторінки за тегом <h1>
    # title_text = title_locator.evaluate("node => node.innerText")
    # print("Заголовок сторінки:", title_text)

    # male_checkbox_locator = page.locator("input[name='male']")  # Знаходимо чекбокс за атрибутом 'name'
    # is_checked = male_checkbox_locator.evaluate("node => node.checked")
    # print("Чекбокс 'Male' обраний:", is_checked)
    # ! 16 get_by_role - Позволяет находить элементы по их роли ARIA, атрибутам ARIA и доступному имени.

    #    page.get_by_role("checkbox", name="female").check()
    #    page.get_by_role("button", name="submit").click()

    #    expect(page.get_by_role("heading", name="Helloo")).to_be_visible()

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

    # ! 24 frame_locator - При работе с iframe вы можете создать локатор фрейма,
    # ! который будет входить в iframe и позволять находить элементы в этом iframe:


    #locator_iframe = page.frame_locator(f'//iframe')
    #print(locator_iframe)


    # ! 25 highlight - Выделите соответствующий элемент(ы) на экране.
    # ! Полезно для отладки, не фиксируйте код, который использует

    #element = page.locator(f'//button[@class = "btn-primary"]')
    #element.highlight()
    #page.wait_for_timeout(2000)

    # ! 26 hover - Наведите курсор на соответствующий элемент.

    #page.get_by_test_id("directions").hover()

    # ! 27 fill - заповнює інпути
    #page.locator(f'//input[@name="firstname"]').fill('Test')

    # ! 28 filter- Цей метод звужує наявний локатор відповідно до параметрів,
    # !наприклад, фільтрує за текстом. Його можна багаторазово фільтрувати.

    #row_locator = page.locator(f'//div[@class = "btns"]')
    # ...
    #row_locator.filter(has_text="submit").filter(
    #    has=page.get_by_role("button", name="submit")
    #).screenshot()

    # ! 29 focus

    # page.locator(f'//input[@name="age"]').focus()

    # ! 30 inner_html -
    # ul_list = page.locator(f'//ul')
    # print(ul_list.inner_html())
    # повертає html розмітку
    #< li class ="first_li" > first text contains: Text1 </ li >
    #< li title = "second_li" > second text contains: Text2 < / li >
    #< li > third text contains: Text3 < / li >

    # ! 31 inner_text повертає рядок тексту

    # text = page.locator(f'//p')
    # print(text.inner_text())

    # ! 32 input_value - Повертає значення для відповідного елемента <input>, <textarea> або <select>.

    #page.locator(f'//input[@name= "firstname"]').fill("test")
    #check_input = page.locator(f'//input[@name= "firstname"]').input_value()
    #print(check_input)

    # ! 33 is_checked - Повертає, чи перевірено елемент.
    # ! Викидає, якщо елемент не є прапорцем або радіобатоном.

    #print(page.locator(f'//input[@id= "male"]').is_checked())
    #print(page.locator(f'//input[@name= "idk"]').is_checked())

    # ! 34 is_disabled - Повертає, чи елемент вимкнено, протилежно включеному.

    #print(page.locator(f'//button[@name="submit"]').is_disabled())
    #print(page.locator(f'//button[@class="btn-disable"]').is_disabled())


    # ! 35 is_editable - Повертає, чи можна редагувати елемент.

    #print(page.locator(f'//input[@name= "firstname"]').is_editable())
    #print(page.locator(f'//ul').is_editable())
    # * який локатор не підставиш завжди виводе тру

    # ! 36 is_enabled - Повертає, чи ввімкнено елемент.

    #print(page.locator(f'//button[@name="submit"]').is_enabled())
    #print(page.locator(f'//button[@class="btn-disable"]').is_enabled())

    # ! 37 is_hidden - Повертає, чи є елемент прихованим або видимим.

    #print(page.get_by_alt_text('nature1').is_hidden())
    #print(page.get_by_alt_text('ball').is_hidden())
    #print(page.locator(f'//img[@class="hidden"]').is_hidden())

    # ! 38 is_visible - Повертає, чи є елемент видимим.
    #print(page.get_by_alt_text('ball').is_visible())
    #print(page.locator(f'//img[@class="hidden"]').is_visible())

    # ! 39 locator - Метод знаходить елемент, який відповідає вказаному селектором у піддереві локатора.
    # ! Він також приймає параметри фільтра, подібні до методу locator.filter().

    #locator_element = page.locator(f'//ul').locator(f'//ul/li[@title="second_li"]')
    #print(locator_element)

    # ! 40 nth - Повертає локатор до n-го відповідного елемента. Він заснований на нулі, nth(0) вибирає перший елемент.

    #some_elem_list = page.locator(f'//ol/li').nth(3).text_content()
    #print(some_elem_list)


    # * 41 or_ Створює локатор, який відповідає будь-якому з двох локаторів
    # page.locator(f'//button[@class="hero-btn btn"]').click()
    # check_box = page.locator(f'//span[@class="check-empty"]')
    #
    # text_name = page.get_by_text("Leave your contacts and we will call you back")
    # expect(check_box.or_(text_name)).to_be_visible()
    # if (text_name.is_visible()):
    #     page.get_by_role("button", name="send").click()
    # check_box.click()

    # page_portf = page.locator('//a[@href="./portfolio.html"]')
    # new_order = page.locator('//button[@class="hero-btn btn"]')
    # new_order.click()
    # dialog = page.get_by_text("Leave your contacts and we will call you back")
    # expect(dialog.or_(page_portf)).to_be_visible()
    # if (dialog.is_visible()):
    #     page.get_by_role("button", name="close").click()
    # page_portf.click()

    # * не підходе сайт

    # ! 42 press - Фокусує відповідний елемент і натискає комбінацію клавіш.

    #some_element = page.locator(f'//input[@name="firstname"]')
    #some_element.fill("NAME")
    #some_element.press("Tab")

    # ! 43 screenshot - Зробіть скріншот елемента, який відповідає локатору
    #page.locator('//input[@type="file"]').scroll_into_view_if_needed()
    #page.locator('//input[@type="file"]').screenshot(animations="disabled", path="screenshot1.png")



    # ! 44 scroll_into_view_if_needed - Цей метод очікує на перевірку функціональності, а потім намагається прокрутити елемент у поле зору,
    # ! якщо він не повністю видимий, як визначено коефіцієнтом IntersectionObserver.

    #page.locator(f'//input[@type="file"]').scroll_into_view_if_needed()


    # ! 45 select_option Вибирає параметр або параметри в <select>.

    #page.locator(f'//select').select_option("Red")

    # ! 46 select_text - Цей метод очікує перевірки функціональності, потім фокусує елемент і вибирає весь його текстовий вміст.

    #page.locator(f'//ul').select_text()


    # ! 47 set_checked - Встановити стан прапорця або радіоелемента

    #page.locator(f'//input[@name="female"]').set_checked(True)

    # ! 48 set_input_files - Завантажте файл або декілька файлів у <input type=file>.

    # page.locator(f'//input[@type="file"]').set_input_files('text.txt')


    # * 49 tap - Виконайте жест торкання елемента, який відповідає локатору
    # * Цей локатор не виконується тому, що сторінка не підтримує операцію "tap"

    # page.locator(f'//input[@type="file"]').tap()


    # ! 50 text_content - Returns the node.textContent.

    #content = page.locator(f'//ol/li')
    #last_li = content.last.text_content()
    #first_li = content.first.text_content()
    #print(last_li)
    #print(first_li)

    # ! 51 type - Фокусує елемент, а потім надсилає події натискання клавіші,
    # ! натискання/введення та натискання клавіші для кожного символу в тексті.

    #element = page.get_by_label("firstname")
    #element.type("Alyonka")


    # ! 52 uncheck - Переконайтеся, що прапорець або перемикач знято.

    #page.locator(f'//input[@name="male"]').uncheck()

    # ! 53 wait_for - Повертає, якщо елемент, указаний локатором, задовольняє параметр стану.

    #page.locator(f'//div[@class="image"]/img').wait_for()

    # ! 54 first - Returns locator to the first matching element.

    #list_first = page.locator(f'//ol/li').first.text_content()
    #print(list_first)


    # ! 55 last - Returns locator to the last matching element.

    #list_last = page.locator(f'//ol/li').last.text_content()
    #print(list_last)


    # ! 56 page - Сторінка, якій належить цей локатор.

    #print(page.locator(f'//ol/li').page)















