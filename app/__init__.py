#from flask import Flask
from flask import request, redirect, render_template, Flask

#app = Flask(__name__)
app=Flask(__name__,template_folder='template')

from app import upload