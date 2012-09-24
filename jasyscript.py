# Jasy Compat - JavaScript Foundation
# Copyright 2012 Zynga Inc.

@task
def clean():
    """Clean"""

    session.clean()
    Repository.clean()
    
    
@task
def distclean():
    """Distclean"""

    session.clean()
    Repository.distclean()
    

@task
def build():
    """Build"""

    assetManager = AssetManager(session).addBuildProfile()
    outputManager = OutputManager(session, assetManager)

    outputManager.storeKernel("$prefix/script/kernel.js", debug=True)
    outputManager.deployAssets(["jasycompat.Main"])

    classes = Resolver(session).addClassName("jasycompat.Main").getSortedClasses()
    outputManager.storeCompressed(classes, "$prefix/script/main.js")
    
    FileManager(session).updateFile("source/index.html", "$prefix/index.html")
    
    
@task
def source():
    """Source"""

    assetManager = AssetManager(session).addSourceProfile()
    outputManager = OutputManager(session, assetManager)

    outputManager.storeKernel("$prefix/script/kernel.js", debug=True)

    classes = Resolver(session).addClassName("jasycompat.Main").getSortedClasses()
    outputManager.storeLoader(classes, "$prefix/script/main.js")
