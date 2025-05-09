class animal:

    def animalAttribute(self):
        print('grantparent')

class human(animal):

    def humanAttribute(self):
        print('parent')


class selected(human):

    def trialAligibility(self):
        print('child')


sel = selected()

print(sel.animalAttribute())
print(sel.humanAttribute())
print(sel.trialAligibility())

