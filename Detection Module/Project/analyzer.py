#!/usr/bin/python

""" Brenno T. De Faria """
""" Projeto de IC """
""" Modulo De Detecao Imagem.0 """

import numpy as np
import cv2


def backgroundSubstraction(back, frame):
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    diff_frame = cv2.absdiff(back, frame)
    cv2.multiply(diff_frame, diff_frame, diff_frame, 2)

    return diff_frame



def histogram(diff_frame):
    hist = cv2.calcHist([diff_frame], [0], None, [256], [0, 256])
    return hist
