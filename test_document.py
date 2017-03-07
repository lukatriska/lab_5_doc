import document

document = document.Document()

# shows insertion
document.insert("p")
document.insert("r")
document.insert("o")
document.insert("d")
document.insert("i")
document.insert("g")
document.insert("y")
print(document.string)

# shows moving back
document.back()
document.back()
document.back()
document.back()
document.insert("X")
print(document.string)

# shows moving forwards
document.forward()
document.forward()
document.insert("X")
print(document.string)

# shows moving home
document.cursor.home()
document.insert("X")
print(document.string)

# shows moving to the end
document.cursor.end()
document.insert("X")
print(document.string)

# shows deleting a character
document.back()
document.back()
document.delete()
print(document.string)

# shows saving a file
document.save("test")
