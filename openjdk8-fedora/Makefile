#
# Copyright (C) 2013 Cloudius Systems, Ltd.
#
# This work is open source software, licensed under the terms of the
# BSD license as described in the LICENSE file in the top-level directory.
#

.PHONY: module clean

jvm_dir=install/usr/lib/jvm

java_version=$(shell ./latest.sh java-1.8.0-openjdk-headless x86_64)
java_dir=http://mirrors.kernel.org/fedora/development/rawhide/x86_64/os/Packages/j/
java_fullname=java-1.8.0-openjdk-headless-$(java_version).x86_64.rpm

tzdata_version=$(shell ./latest.sh tzdata-java noarch)
tzdata_dir=http://mirrors.kernel.org/fedora/development/rawhide/x86_64/os/Packages/t/
tzdata_fullname=tzdata-java-$(tzdata_version).noarch.rpm

upstream/$(java_fullname):
	mkdir -p upstream
	wget -O upstream/$(java_fullname) $(java_dir)$(java_fullname)

upstream/$(tzdata_fullname):
	mkdir -p upstream
	wget -O upstream/$(tzdata_fullname) $(tzdata_dir)$(tzdata_fullname)

module: upstream/$(java_fullname) upstream/$(tzdata_fullname)
	rm -rf install
	mkdir -p install
	rpm2cpio upstream/$(java_fullname) | (cd install && cpio -id)
	ln -sf java-1.8.0-openjdk-$(java_version).x86_64 $(jvm_dir)/java
	rm -rf $(jvm_dir)/java/jre/lib/security/cacerts
	rm -rf $(jvm_dir)/java/jre/lib/audio/*
	rpm2cpio upstream/$(tzdata_fullname) | (cd install && cpio -id)

clean:
	rm -rf upstream install
