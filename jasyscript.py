# Jasy Compat - JavaScript Foundation
# Copyright 2012 Zynga Inc.

@task("Clean")
def clean():
    session.clearCache()
    
    
@task("Distclean")
def distclean():
    session.clearCache()
    removeDir("build")
    removeDir("source/script")
    

@task("Build")
def build():
    resolver = Resolver().addClassName("compatty.Main")
    
    asset = AssetManager(resolver.getIncludedClasses())
    kernelClasses = storeKernel("script/kernel.js", assets=asset.exportBuild())
    
    resolver.excludeClasses(kernelClasses)
    storeCompressed("script/main.js", Sorter(resolver).getSortedClasses())
    copyFile("source/index.html", "index.html")
    
    
@task("Source")
def source():
    resolver = Resolver().addClassName("compatty.Main")

    asset = AssetManager(resolver.getIncludedClasses())
    kernelClasses = storeKernel("script/kernel.js", assets=asset.exportSource())

    resolver.excludeClasses(kernelClasses)
    storeLoader("script/main.js", Sorter(resolver).getSortedClasses())
