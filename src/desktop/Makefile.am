MAINTAINERCLEANFILES = $(srcdir)/Makefile.in

eudatarootdir = $(datarootdir)/ecryptfs-utils
dist_eudataroot_DATA = ecryptfs-record-passphrase

desktopdir = $(datarootdir)/ecryptfs-utils

desktop_in_files = \
	ecryptfs-mount-private.desktop.in \
	ecryptfs-setup-private.desktop.in

desktop_DATA = $(desktop_in_files:.desktop.in=.desktop)

@INTLTOOL_DESKTOP_RULE@
