################################################################################
## A more advanced Standalone Jython Application Jar
## Based on the original example By Ryan McGuire (www.EnigmaCurry.com)
## Modified and expanded upon by Pete Dickson (www.noskcid.com)
################################################################################

This application does very little. It produces a simple GUI using Java's 
Swing Framework, which loads up an image contained within the Jar and
displays the current date using Python's Standard Library.

This example builds upon Ryan McGuire's original example 'A self contained, executable, Jython Excel dohicky'. 

The goal of this example is to demonstrate two things:
1. The Python Standard Library working.
2. The ability to store and thus utilise resources such as images within the Jar

A standalone Jar (including resources) will be produced containing the
Application. The Jar requires no external dependancies other than a JVM on the
host computer.

A quick thank you to FastIcon.com for providing the example image used in this example.
(More information in LICENSE.txt)

To base your own project off this example you should understand how
this package is organized:

 * /src 
    Put all of your Jython source code here

 * /lib
    Put any .jar dependancies in this directory. Any .jar in this
    directory will automatically be loaded when the application starts
    so there is no need to mess with a CLASSPATH.

    This sample project has two dependancies:

      * Jython itself (jython.jar)
      * The Python Standard Library (modules.jar)
	  
    Since this is a Jython project, the jython jar is required in this
    directory. This Jython jar does not contain the Python Standard Library
    as, when packaged as a standalone Jar, Jython cannot find it in this location.
    Instead the Jython /Lib directory has been compressed into (modules.jar)
    and is stored separately to the Jython Distribution, the location of
    the standard library is made known to Jython by adding it to the classpath
    in Main.java.

 * /java-src
    This is meant to be a Python project, but since this is Jython,
    there's no reason you can't include some Java code as well, so put
    that in this directory.

    One thing that is required in this directory is some sort of
    bootstrap mechanism to start your Jython code. You can do that
    however you want, but a sample Main.java is included. If you call
    yours something different, you need to update the Manifest.MF
    option One-Jar-Main-Class.

 * /onejar-src
    Part of the technology which powers this application is the OneJar
    platform (http://one-jar.sourceforge.net/). This takes care of
    loading "jars within jars" which is a problem for the regular Java 
    classloader. You shouldn't need to touch this code unless
    you want to upgrade to a later version for some reason.

    OneJar is accompanied by it's own free license called
    one-jar-license.txt. In order to comply with this license, the
    license is automatically built into any .jar that this package builds.

 * /resources
    This is where to store anything that you want packaged with the application
    that it may require. This may be images or audio for example. This folder
    is copied directly into the root of the standalone Jar.

    For info on how to load resources within the Jar, see the example Jython
    Script (src/__init__.py)


Building the app:

    You need Apache Ant installed. It should be sufficient to just 
    run 'ant' in the same directory as build.xml
    
    Ant should create a new jar file called JythonApplication.jar
    which you can then run:

        java -jar JythonApplication.jar


Building Jython:
  
    Jython is already included in this distribution, but when new
    versions of Jython come out, you may wish to upgrade. To do so
	simply download the latest version of Jython and copy (jython.jar)
	into the /lib directory.
	
	
    
