import random, time, tweepy

from os import environ
from flask import Flask

app = Flask(__name__)
app.run(environ.get('PORT'))

app.run(host= '0.0.0.0', port=environ.get('PORT'))

CONSUMER_KEY = 'Wgtyo7nAmSt6JxpvAR5kyUvAV'
CONSUMER_SECRET = 'zYGQ41czCmMbXjHHvCx7aiWWmuk8T2pPRcMYgca3ZUpKPY35qK'
ACCESS_KEY = '1189237778036547585-atr7slv7ikpus1jKImG8q1EFQdZq28'
ACCESS_SECRET = 'T1aXrJcUXzAbXvSkGcRjt0TW7mPoUpcwlyg7S4BVt1Ce0'

auth = tweepy.OAuthHandler('Wgtyo7nAmSt6JxpvAR5kyUvAV', 'zYGQ41czCmMbXjHHvCx7aiWWmuk8T2pPRcMYgca3ZUpKPY35qK')
auth.set_access_token('1189237778036547585-atr7slv7ikpus1jKImG8q1EFQdZq28', 'T1aXrJcUXzAbXvSkGcRjt0TW7mPoUpcwlyg7S4BVt1Ce0')
api = tweepy.API(auth)

preamble = ["I celebrate myself, and sing myself, ", "And what I assume you shall assume, ", "For every atom belonging to me as good belongs to you. ", "I loafe and invite my soul, ", "I lean and loafe at my ease observing a spear of summer grass. ", "My tongue, every atom of my blood, form’d from this soil, this air, ", "Born here of parents born here from parents the same, and their parents the same, ", "I, now thirty-seven years old in perfect health begin, ", "Hoping to cease not till death. ", "Creeds and schools in abeyance, ", "Retiring back a while sufficed at what they are, but never forgotten, ", "I harbor for good or bad, I permit to speak at every hazard, ","Nature without check with original energy. "]

action = ["Houses and rooms are full of perfumes, the shelves are crowded with perfumes, ", "I breathe the fragrance myself and know it and like it, ", "The distillation would intoxicate me also, but I shall not let it. ","The atmosphere is not a perfume, it has no taste of the distillation, it is odorless, ", "It is for my mouth forever, I am in love with it, ", "I will go to the bank by the wood and become undisguised and naked, ", "I am mad for it to be in contact with me. ", "The smoke of my own breath, ", "Echoes, ripples, buzz’d whispers, love-root, silk-thread, crotch and vine, ", "My respiration and inspiration, the beating of my heart, the passing of blood and air through my lungs, ", "The sniff of green leaves and dry leaves, and of the shore and dark-color’d sea-rocks, and of hay in the barn, ", "The sound of the belch’d words of my voice loos’d to the eddies of the wind, ", "A few light kisses, a few embraces, a reaching around of arms, ", "The play of shine and shade on the trees as the supple boughs wag, ", "The delight alone or in the rush of the streets, or along the fields and hill-sides, ", "The feeling of health, the full-noon trill, the song of me rising from bed and meeting the sun. ", "Have you reckon’d a thousand acres much? have you reckon’d the earth much? ", "Have you practis’d so long to learn to read? ", "Have you felt so proud to get at the meaning of poems? ", "Stop this day and night with me and you shall possess the origin of all poems, ", "You shall possess the good of the earth and sun, (there are millions of suns left,) ", "You shall no longer take things at second or third hand, nor look through the eyes of the dead, nor feed on the spectres in books, ", "You shall not look through my eyes either, nor take things from me, ", "You shall listen to all sides and filter them from your self. "]

adjective = ["I have heard what the talkers were talking, the talk of the beginning and the end, ", "But I do not talk of the beginning or the end. ", "There was never any more inception than there is now, ", "Nor any more youth or age than there is now, ", "And will never be any more perfection than there is now, ", "Nor any more heaven or hell than there is now. ", "Urge and urge and urge, ", "Always the procreant urge of the world. ",  "Out of the dimness opposite equals advance, always substance and increase, always sex, ", "Always a knit of identity, always distinction, always a breed of life. ", "To elaborate is no avail, learn’d and unlearn’d feel that it is so. ", "Sure as the most certain sure, plumb in the uprights, well entretied, braced in the beams, ", "Stout as a horse, affectionate, haughty, electrical, ", "I and this mystery here we stand. ", "Clear and sweet is my soul, and clear and sweet is all that is not my soul. ", "Lack one lacks both, and the unseen is proved by the seen, ", "Till that becomes unseen and receives proof in its turn. ", "Showing the best and dividing it from the worst age vexes age,", "Knowing the perfect fitness and equanimity of things, while they discuss I am silent, and go bathe and admire myself. ", "Welcome is every organ and attribute of me, and of any man hearty and clean, ", "Not an inch nor a particle of an inch is vile, and none shall be less familiar than the rest. ", "I am satisfied—I see, dance, laugh, sing; ", "As the hugging and loving bed-fellow sleeps at my side through the night, and withdraws at the peep of the day with stealthy tread, ", "Leaving me baskets cover’d with white towels swelling the house with their plenty, ", "Shall I postpone my acceptation and realization and scream at my eyes, ", "That they turn from gazing after and down the road, ", "And forthwith cipher and show me to a cent, ", "Exactly the value of one and exactly the value of two, and which is ahead? "]

noun = ["Trippers and askers surround me.", "People I meet, the effect upon me of my early life or the ward and city I live in, or the nation.", "The latest dates, discoveries, inventions, societies, authors old and new.", "My dinner, dress, associates, looks, compliments, dues.", "The real or fancied indifference of some man or woman I love.", "The sickness of one of my folks or of myself, or ill-doing or loss or lack of money, or depressions or exaltations.", "Battles, the horrors of fratricidal war, the fever of doubtful news, the fitful events.", "These come to me days and nights and go from me again.", "But they are not the Me myself.", "Apart from the pulling and hauling stands what I am.", "Stands amused, complacent, compassionating, idle, unitary.", "Looks down, is erect, or bends an arm on an impalpable certain rest,", "Looking with side-curved head curious what will come next.", "Both in and out of the game and watching and wondering at it.", "Backward I see in my own days where I sweated through fog with linguists and contenders.", "I have no mockings or arguments, I witness and wait."]

import random

def sentencemaker():
	return random.choice(preamble)+"\n"+random.choice(action)+"\n"+random.choice(adjective)+"\n"+random.choice(noun)

while True:
    postthis = sentencemaker()
    if len(postthis) <= 280:
        api.update_status(status=postthis)
        print postthis
        time.sleep(3600) 
