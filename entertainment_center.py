#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 17 14:21:39 2016

@author: Ryan
"""
import fresh_tomatoes
import media

interstellar = media.Movie("Interstellar", 
                           "A brilliant NASA physicist is working on plans to save mankind by transporting Earth's population to a new home via a wormhole.",
                           "http://t1.gstatic.com/images?q=tbn:ANd9GcRf61mker2o4KH3CbVE7Zw5B1-VogMH8LfZHEaq3UdCMLxARZAB",
                           "https://www.youtube.com/watch?v=sRLc9OlrZZw")

pan = media.Movie("Pan's Labyrinth",
                  "Ofelia encounters the faun Pan, who tells her that she is a legendary lost princess and must complete three dangerous tasks in order to claim immortality.",
                  "http://www.gstatic.com/tv/thumb/movieposters/162074/p162074_p_v8_ab.jpg",
                  "https://www.youtube.com/watch?v=EqYiSlkvRuw")

shadows = media.Movie("What We Do in the Shadows",
                          "Vampire housemates try to cope with the complexities of modern life and show a newly turned hipster some of the perks of being undead.",
                          "http://t1.gstatic.com/images?q=tbn:ANd9GcTb1oWD0EwTDmLFAu0i1IIgAQLSCITuuVeExzzWpIE14xiVm1B7",
                          "https://www.youtube.com/watch?v=Cv568AzZ-i8")

moonrise = media.Movie("Moonrise Kingdom",
                       "The year is 1965, and the residents of New Penzance, an island off the coast of New England, inhabit a community that seems untouched by some of the bad things going on in the rest of the world. ",
                       "http://t1.gstatic.com/images?q=tbn:ANd9GcTc9Qfqux_R9ycASZUOHD0R-1wNYeGYg-0Y9ICVmKOKekAGhplc",
                       "https://www.youtube.com/watch?v=_eOI3AamSm8")

empire = media.Movie("Star Wars: The Empire Strikes Back",
                     "Luke Skywalker, Han Solo, Princess Leia and Chewbacca face attack by the Imperial forces and its AT-AT walkers on the ice planet Hoth.",
                     "http://a.dilcdn.com/bl/wp-content/uploads/sites/6/2015/07/ESB-Special-Edeition.jpg",
                     "https://www.youtube.com/watch?v=xESiohGGP7g")

twotowers = media.Movie("The Lord of the Rings: The Two Towers",
                        "Follows the continuing quest of Frodo (Elijah Wood) and the Fellowship to destroy the One Ring.",
                        "http://www.gstatic.com/tv/thumb/movieposters/30793/p30793_p_v8_am.jpg",
                        "https://www.youtube.com/watch?v=2dlRvAjU_RI")

movies=[interstellar, pan, shadows, moonrise, empire, twotowers]
fresh_tomatoes.open_movies_page(movies)

#blackmirror =
        #https://www.youtube.com/watch?v=THP9YQ3WT1k
        
#strangerthings =        
        #https://www.youtube.com/watch?v=XWxyRG_tckY