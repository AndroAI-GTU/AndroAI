import os

project_structure = {
        "app": {
            "src": {
                "androidTest": {
                    "java": {
                        "com": {
                            "androai": {
                                "ExampleInstrumentedTest.java": '''package com.androai.myandroidapp;

import android.content.Context;

import androidx.test.platform.app.InstrumentationRegistry;
import androidx.test.ext.junit.runners.AndroidJUnit4;

import org.junit.Test;
import org.junit.runner.RunWith;

import static org.junit.Assert.*;

@RunWith(AndroidJUnit4.class)
public class ExampleInstrumentedTest {
    @Test
    public void useAppContext() {
        // Context of the app under test.
        Context appContext = InstrumentationRegistry.getInstrumentation().getTargetContext();
        assertEquals("com.androai.myandroidapp", appContext.getPackageName());
    }
}
'''
                            }
                        }
                    }
                },
                "main": {
                    "AndroidManifest.xml": '''<manifest xmlns:android="http://schemas.android.com/apk/res/android"
    package="com.androai.myandroidapp">

    <application
        android:allowBackup="true"
        android:icon="@mipmap/ic_launcher"
        android:label="@string/app_name"
        android:roundIcon="@mipmap/ic_launcher_round"
        android:supportsRtl="true"
        android:theme="@style/Theme.MyAndroidApp">
        <activity android:name=".MainActivity">
            <intent-filter>
                <action android:name="android.intent.action.MAIN" />
                <category android:name="android.intent.category.LAUNCHER" />
            </intent-filter>
        </activity>
    </application>

</manifest>
''',
                    "java": {
                        "com": {
                            "androai": {
                                "MainActivity.java": '''package com.androai.myandroidapp;

import android.os.Bundle;
import androidx.appcompat.app.AppCompatActivity;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
    }
}
'''
                            }
                        }
                    },
                    "res": {
                        "layout": {
                            "activity_main.xml": '''<?xml version="1.0" encoding="utf-8"?>
<RelativeLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:padding="16dp">

    <TextView
        android:id="@+id/textView"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="Hello I am AndroAI"
        android:textSize="18sp"
        android:layout_centerInParent="true"/>
</RelativeLayout>
'''
                        },
                        "values": {
                            "strings.xml": '''<resources>
    <string name="app_name">MyAndroidApp</string>
    <string name="hello_world">Hello I am AndroAI</string>
</resources>
'''
                        }
                    }
                },
                "test": {
                    "java": {
                        "com": {
                            "androai": {
                                "ExampleUnitTest.java": '''package com.androai.myandroidapp;

import org.junit.Test;

import static org.junit.Assert.*;

public class ExampleUnitTest {
    @Test
    public void addition_isCorrect() {
        assertEquals(4, 2 + 2);
    }
}
'''
                            }
                        }
                    }
                }
            },
            "build.gradle": '''plugins {
    id 'com.android.application'
}

android {
    compileSdkVersion 30
    defaultConfig {
        applicationId "com.androai.myandroidapp"
        minSdkVersion 21
        targetSdkVersion 30
        versionCode 1
        versionName "1.0"

        testInstrumentationRunner "androidx.test.runner.AndroidJUnitRunner"
    }
    buildTypes {
        release {
            minifyEnabled false
            proguardFiles getDefaultProguardFile('proguard-android-optimize.txt'), 'proguard-rules.pro'
        }
    }
}

dependencies {
    implementation 'androidx.appcompat:appcompat:1.3.1'
    implementation 'com.google.android.material:material:1.4.0'
    implementation 'androidx.constraintlayout:constraintlayout:2.1.0'
    testImplementation 'junit:junit:4.13.2'
    androidTestImplementation 'androidx.test.ext:junit:1.1.3'
    androidTestImplementation 'androidx.test.espresso:espresso-core:3.4.0'
}
''',
            "proguard-rules.pro": '''# Add your ProGuard rules here
# By default, the flags in this file are appended to flags specified
# in /usr/share/proguard/proguard-android.txt
# You can edit the include path and order by changing the proguardFiles
# directive in build.gradle.
'''
        },
        "build.gradle": '''// Top-level build file where you can add configuration options common to all sub-projects/modules.
buildscript {
    repositories {
        google()
        mavenCentral()
    }
    dependencies {
        classpath "com.android.tools.build:gradle:8.0.2"
    }
}

allprojects {
    repositories {
        google()
        mavenCentral()
    }
}

task clean(type: Delete) {
    delete rootProject.buildDir
}
''',
        "gradle": {
            "wrapper": {
                "gradle-wrapper.properties": r'''distributionBase=GRADLE_USER_HOME
distributionPath=wrapper/dists
zipStoreBase=GRADLE_USER_HOME
zipStorePath=wrapper/dists
distributionUrl=https\://services.gradle.org/distributions/gradle-8.0.2-all.zip
'''
            }
        },
        "gradle.properties": '''org.gradle.jvmargs=-Xmx2048m -Dkotlin.daemon.jvm.options="-Xmx2048m"
''',
        "gradlew": r'''#!/usr/bin/env sh

##############################################################################
##
##  Gradle start up script for UN*X
##
##############################################################################

# Add default JVM options here. You can also use JAVA_OPTS and GRADLE_OPTS to pass JVM options to this script.
DEFAULT_JVM_OPTS=""

APP_NAME="Gradle"
APP_BASE_NAME=$(basename "$0")

# shellcheck disable=SC2046
APP_HOME=$(cd "$(dirname "$0")"; cd "../gradle"; pwd)

# Add default JVM options here. You can also use JAVA_OPTS and GRADLE_OPTS to pass JVM options to this script.
DEFAULT_JVM_OPTS=""

# Use the maximum available, or set MAX_FD != -1 to use that value.
MAX_FD="maximum"

warn () {
    echo "$*" >&2
}

die () {
    echo
    echo "$*" >&2
    echo
    exit 1
}

# OS specific support (must be 'true' or 'false').
cygwin=false
msys=false
darwin=false
case "$(uname)" in
    CYGWIN* )
        cygwin=true
        ;;
    MINGW* )
        msys=true
        ;;
    Darwin* )
        darwin=true
        ;;
esac

# For Cygwin or MSYS, switch paths to Windows format before running java
if $cygwin || $msys; then
    [ -n "$JAVA_HOME" ] && JAVA_HOME=$(cygpath --unix "$JAVA_HOME")
    [ -n "$CLASSPATH" ] && CLASSPATH=$(cygpath --path --unix "$CLASSPATH")
fi

CLASSPATH=$APP_HOME/gradle-wrapper.jar

if [ -n "$JAVA_HOME" ] ; then
    if [ -x "$JAVA_HOME/jre/sh/java" ] ; then
        JAVACMD="$JAVA_HOME/jre/sh/java"
    else
        JAVACMD="$JAVA_HOME/bin/java"
    fi
    if [ ! -x "$JAVACMD" ] ; then
        die "ERROR: JAVA_HOME is set to an invalid directory: $JAVA_HOME

Please set the JAVA_HOME variable in your environment to match the
location of your Java installation."
    fi
else
    JAVACMD=$(which java)
    if [ -z "$JAVACMD" ] ; then
        die "ERROR: JAVA_HOME is not set and no 'java' command could be found in your PATH.

Please set the JAVA_HOME variable in your environment to match the
location of your Java installation."
    fi
fi

# Increase the maximum file descriptors if we can.
if [ "$cygwin" = false ] && [ "$msys" = false ] ; then
    MAX_FD_LIMIT=$(ulimit -H -n)
    if [ $? -eq 0 ] ; then
        if [ "$MAX_FD" = "maximum" ] || [ "$MAX_FD" = "$MAX_FD_LIMIT" ] ; then
            MAX_FD=$MAX_FD_LIMIT
        fi
        ulimit -n "$MAX_FD" || warn "Could not set maximum file descriptor limit: $MAX_FD"
    else
        warn "Could not query maximum file descriptor limit: $MAX_FD_LIMIT"
    fi
fi

# For Darwin, add options to specify how the application should appear in the dock
if $darwin; then
    GRADLE_OPTS="$GRADLE_OPTS '-Xdock:name=$APP_NAME' '-Xdock:icon=$APP_HOME/media/gradle.icns'"
fi

# Escape application args for windows shell
case "$APP_BASE_NAME" in
    * )
        APP_ARGS=$(echo "$@" | sed 's/\([\\"]\)/\\\1/g')
        ;;
esac

# Collect all arguments for the java command, following the shell quoting and escaping conventions.
ALL_JVM_OPTS=$DEFAULT_JVM_OPTS
ALL_JVM_OPTS=$ALL_JVM_OPTS' '"$JAVA_OPTS"
ALL_JVM_OPTS=$ALL_JVM_OPTS' '"$GRADLE_OPTS"
ALL_JVM_OPTS=$ALL_JVM_OPTS' '"$APP_ARGS"

# Launch the application.
exec "$JAVACMD" $ALL_JVM_OPTS -classpath "$CLASSPATH" org.gradle.wrapper.GradleWrapperMain "$@"
''',
        "gradlew.bat": r'''@echo off
setlocal

set DIRNAME=%~dp0
if "%DIRNAME%" == "" set DIRNAME=.
set APP_BASE_NAME=%~n0
set APP_HOME=%DIRNAME%\..

@rem Add default JVM options here. You can also use JAVA_OPTS and GRADLE_OPTS to pass JVM options to this script.
set DEFAULT_JVM_OPTS=

if defined JAVA_HOME goto findJavaFromJavaHome

set JAVA_EXE=java.exe
%JAVA_EXE% -version >NUL 2>&1
if "%ERRORLEVEL%" == "0" goto execute

echo.
echo ERROR: JAVA_HOME is not set and no 'java' command could be found in your PATH.
echo.
echo Please set the JAVA_HOME variable in your environment to match the
echo location of your Java installation.
goto fail

:findJavaFromJavaHome
set JAVA_HOME=%JAVA_HOME:"=%

set JAVA_EXE=%JAVA_HOME%/bin/java.exe

if exist "%JAVA_EXE%" goto execute

set JAVA_EXE=%JAVA_HOME%\bin\java.exe

if exist "%JAVA_EXE%" goto execute

echo.
echo ERROR: JAVA_HOME is set to an invalid directory: %JAVA_HOME%
echo.
echo Please set the JAVA_HOME variable in your environment to match the
echo location of your Java installation.
goto fail

:execute
@rem Add default JVM options here. You can also use JAVA_OPTS and GRADLE_OPTS to pass JVM options to this script.
set DEFAULT_JVM_OPTS=

set CLASSPATH=%APP_HOME%\gradle\wrapper\gradle-wrapper.jar

@rem Collect all arguments for the java command, following the shell quoting and escaping conventions.
set ALL_JVM_OPTS=%DEFAULT_JVM_OPTS%
set ALL_JVM_OPTS=%ALL_JVM_OPTS% %JAVA_OPTS%
set ALL_JVM_OPTS=%ALL_JVM_OPTS% %GRADLE_OPTS%

"%JAVA_EXE%" %ALL_JVM_OPTS% org.gradle.wrapper.GradleWrapperMain %CMD_LINE_ARGS%

:end
'''
}

def create_project_structure(base_path, structure):

    for name, content in structure.items():

        path = os.path.join(base_path, name)

        if isinstance(content, dict):

            os.makedirs(path, exist_ok=True)
            create_project_structure(path, content)

        else:

            with open(path, 'w') as f:
                
                f.write(content)

project_dir = "MyAndroidApp"
create_project_structure(project_dir, project_structure)
