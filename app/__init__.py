#from flask import Flask
from flask import request, redirect, render_template, Flask

#app = Flask(__name__)

from app import upload

application=Flask(__name__,template_folder='template')