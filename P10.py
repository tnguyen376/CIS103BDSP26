def main():
    thetext = '''
        Python was conceived in the late 1980's by Netherlands programmer
Guido Van Rossum and rolled out in 1991. Developing the language
was a hobby project for Van Rossum to keep him occupied over
Christmas, though he soon began implementing the language at
his employer Centrum Wiskunde & Informatica (CWI). The name of
the language was inspired by Monty Python's Flying Circus, and
today users users of this code often work in references to Monty Python.
Python is one of the most popular programming languages in the
world. As a scripting language that can automate a complex series
of tasks, Python is used on the back end of many web applications,
games, and digital and animated special effects. Sites like YouTube
and Instagram are among some of the titans that rely on this
language to support both front-end and back-end functionality.
        '''
    print('Original text')
    print(thetext)
    print('Length of original text:', len(thetext))

    stripped_text = thetext.strip()
    print('Length after strip:', len(stripped_text))

    the_count = stripped_text.count('the')
    print('Number of times "the" appears:', the_count)

    if 'little' in stripped_text:
        print('"little" was found in the text.')
    else:
        print('"little" was NOT found in the text.')

    if 'titan' in stripped_text:
        print('"titan" was found in the text.')
    else:
        print('"titan" was NOT found in the text.')

    appl_position = stripped_text.find('appl')
    print('Position of "appl":', appl_position)

    thetext2 = stripped_text
    thetext2 = thetext2.replace('Python', 'PYTHON')
    print('Text after replacing "Python" with "PYTHON":')
    print(thetext2)
    # put assignment statements here

main()
