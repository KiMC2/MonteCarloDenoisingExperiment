import time
import cv2
import numpy as numpy
import tensorflow as tf

from src.initialize import build_option


def main():
  option = build_option()

  global_step = tf.train.get_or_create_global_step()
