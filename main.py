
from pyscript import display
from js import document

# assigning images
img = {
    (7,  "ruby"):    ("yellow tigers.jpg",   "Yellow Tigers"),
    (7,  "emerald"): ("green hornets.jpg",   "Green Hornets"),
    (8,  "ruby"):    ("blue bears.jpg",      "Blue Bears"),
    (8,  "emerald"): ("red bulldogs.jpg",    "Red Bulldogs"),
    (9,  "ruby"):    ("blue bears.jpg",      "Blue Bears"),
    (9,  "emerald"): ("red bulldogs.jpg",    "Red Bulldogs"),
    (10, "ruby"):    ("yellow tigers.jpg",   "Yellow Tigers"),
    (10, "emerald"): ("green hornets.jpg",   "Green Hornets"),
}


def intrams_checker(_event=None):
    # clear
    document.getElementById('output').innerHTML = ''
    document.getElementById('image').innerHTML  = ''

    # buttons
    register = document.querySelector('input[name="registration"]:checked')
    clear    = document.querySelector('input[name="clearance"]:checked')

    # gentle reminder
    if register is None or clear is None:
        display("I asked you a question", target="output")
        return

    # check
    registration = register.value
    clearance    = clear.value

    # grade and section
    grade_node   = document.getElementById('grade')
    grade_level  = int(grade_node.value)

    section_node = document.getElementById('section')
    section      = section_node.value

    # more checking
    if registration != 'registered':
        display("u not registered🤨", target='output')
        return

    if clearance != 'cleared':
        display("u fragile😛", target='output')
        return

    # yay
    display("Enjoy Intrams!", target='output')

    # what team you get
    img_src, alt_text = img.get((grade_level, section), (None, None))
    if img_src:
        document.getElementById("image").innerHTML = (
            f"<img src='{img_src}' width='150' alt='{alt_text}'>"
        )