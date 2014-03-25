AUTOMAKE_OPTIONS = subdir-objects

# Only place tests worth of 'make check' here. All other tests are noinst.
dist_check_SCRIPTS = lfs.sh verify-passphrase-sig.sh
check_PROGRAMS = lfs/test verify-passphrase-sig/test

dist_noinst_DATA = tests.rc

dist_noinst_SCRIPTS = $(dist_check_SCRIPTS) \
		      wrap-unwrap.sh

if ENABLE_TESTS
noinst_PROGRAMS = $(check_PROGRAMS) \
		  wrap-unwrap/test
endif

lfs_test_SOURCES = lfs/test.c

verify_passphrase_sig_test_SOURCES = verify-passphrase-sig/test.c
verify_passphrase_sig_test_LDADD = $(top_builddir)/src/libecryptfs/libecryptfs.la

wrap_unwrap_test_SOURCES = wrap-unwrap/test.c
wrap_unwrap_test_LDADD = $(top_builddir)/src/libecryptfs/libecryptfs.la

TESTS = lfs.sh verify-passphrase-sig.sh

