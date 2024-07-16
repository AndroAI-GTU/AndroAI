#!/bin/bash

adb shell am force-stop com.androai.helloworld
adb uninstall com.androai.helloworld
adb install -d ./bin/HelloWorld.apk
adb shell am start -c android.intent.category.LAUNCHER -a android.intent.action.MAIN -n com.androai.helloworld/.MainActivity
