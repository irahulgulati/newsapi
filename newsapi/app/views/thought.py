import random
class thoughts:
    def getThought(self):
        self.thought =[{
            "title":"Move quickly. Now is the time to make progress"
            },{
                "title":"Today is a good day"
            },{
                "title":"Show everyone what you can do"
            }]
        return random.choice(self.thought)
             