#!/usr/bin/env python3

import os
import yaml
import gi
gi.require_version('Gtk', '3.0') 
gi.require_version('AppIndicator3', '0.1')
from gi.repository import Gtk as gtk, AppIndicator3 as appindicator
from pathlib import Path

ICON_PATH='/usr/share/icons/hicolor/96x96/apps/goa-account-google.png'

def menu():
	menu = gtk.Menu()

	drive_push = gtk.MenuItem('Push')
	drive_push.connect('activate', drivePush)
	menu.append(drive_push)

	drive_pull = gtk.MenuItem('Pull')
	drive_pull.connect('activate', drivePull)
	menu.append(drive_pull)

	Separator = gtk.SeparatorMenuItem()
	menu.append(Separator)

	exittray = gtk.MenuItem('Quit')
	exittray.connect('activate', quit)
	menu.append(exittray)

	menu.show_all()
	return menu


def drivePull(_):
	global drive_dir

def drivePush(_):
	global drive_dir
	os.system("x-terminal-emulator -e \'drive-google push " + drive_dir + ' && read\'')

def quit(_):
	gtk.main_quit()


with open(str(Path.home()) + '/.config/drive_google_tray.yaml') as file:
	config = yaml.load(file, Loader=yaml.FullLoader)
	
drive_dir = config['drive_dir']
indicator = appindicator.Indicator.new("customtray", ICON_PATH, appindicator.IndicatorCategory.APPLICATION_STATUS)
indicator.set_status(appindicator.IndicatorStatus.ACTIVE)
indicator.set_menu(menu())
gtk.main()

