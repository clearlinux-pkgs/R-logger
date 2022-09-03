#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-logger
Version  : 0.2.2
Release  : 7
URL      : https://cran.r-project.org/src/contrib/logger_0.2.2.tar.gz
Source0  : https://cran.r-project.org/src/contrib/logger_0.2.2.tar.gz
Summary  : A Lightweight, Modern and Flexible Logging Utility
Group    : Development/Tools
License  : AGPL-3.0
BuildRequires : buildreq-R

%description
# logger
[![Project Status: Active – The project has reached a stable, usable state and is being actively developed.](https://www.repostatus.org/badges/latest/active.svg)](https://www.repostatus.org/#active) [![CRAN](https://www.r-pkg.org/badges/version/logger)](https://cran.r-project.org/package=logger) [![Build Status](https://travis-ci.org/daroczig/logger.svg?branch=master)](https://travis-ci.org/daroczig/logger) [![Code Coverage](https://codecov.io/gh/daroczig/logger/branch/master/graph/badge.svg)](https://app.codecov.io/gh/daroczig/logger) [![A Mikata Project](https://mikata.dev/img/badge.svg)](https://mikata.dev)

%prep
%setup -q -c -n logger
cd %{_builddir}/logger

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1641049552

%install
export SOURCE_DATE_EPOCH=1641049552
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library logger
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library logger
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library logger
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc logger || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/logger/DESCRIPTION
/usr/lib64/R/library/logger/INDEX
/usr/lib64/R/library/logger/Meta/Rd.rds
/usr/lib64/R/library/logger/Meta/demo.rds
/usr/lib64/R/library/logger/Meta/features.rds
/usr/lib64/R/library/logger/Meta/hsearch.rds
/usr/lib64/R/library/logger/Meta/links.rds
/usr/lib64/R/library/logger/Meta/nsInfo.rds
/usr/lib64/R/library/logger/Meta/package.rds
/usr/lib64/R/library/logger/Meta/vignette.rds
/usr/lib64/R/library/logger/NAMESPACE
/usr/lib64/R/library/logger/NEWS.md
/usr/lib64/R/library/logger/R/logger
/usr/lib64/R/library/logger/R/logger.rdb
/usr/lib64/R/library/logger/R/logger.rdx
/usr/lib64/R/library/logger/demo-packages/logger-tester-package/DESCRIPTION
/usr/lib64/R/library/logger/demo-packages/logger-tester-package/NAMESPACE
/usr/lib64/R/library/logger/demo-packages/logger-tester-package/R/tester.R
/usr/lib64/R/library/logger/demo-packages/logger-tester-package/man/logger_tester_function.Rd
/usr/lib64/R/library/logger/demo/colors.R
/usr/lib64/R/library/logger/doc/Intro.R
/usr/lib64/R/library/logger/doc/Intro.Rmd
/usr/lib64/R/library/logger/doc/Intro.html
/usr/lib64/R/library/logger/doc/anatomy.R
/usr/lib64/R/library/logger/doc/anatomy.Rmd
/usr/lib64/R/library/logger/doc/anatomy.html
/usr/lib64/R/library/logger/doc/customize_logger.R
/usr/lib64/R/library/logger/doc/customize_logger.Rmd
/usr/lib64/R/library/logger/doc/customize_logger.html
/usr/lib64/R/library/logger/doc/index.html
/usr/lib64/R/library/logger/doc/migration.R
/usr/lib64/R/library/logger/doc/migration.Rmd
/usr/lib64/R/library/logger/doc/migration.html
/usr/lib64/R/library/logger/doc/performance.Rmd
/usr/lib64/R/library/logger/doc/performance.html
/usr/lib64/R/library/logger/doc/r_packages.R
/usr/lib64/R/library/logger/doc/r_packages.Rmd
/usr/lib64/R/library/logger/doc/r_packages.html
/usr/lib64/R/library/logger/doc/write_custom_extensions.R
/usr/lib64/R/library/logger/doc/write_custom_extensions.Rmd
/usr/lib64/R/library/logger/doc/write_custom_extensions.html
/usr/lib64/R/library/logger/help/AnIndex
/usr/lib64/R/library/logger/help/aliases.rds
/usr/lib64/R/library/logger/help/figures/colors.png
/usr/lib64/R/library/logger/help/logger.rdb
/usr/lib64/R/library/logger/help/logger.rdx
/usr/lib64/R/library/logger/help/paths.rds
/usr/lib64/R/library/logger/html/00Index.html
/usr/lib64/R/library/logger/html/R.css
/usr/lib64/R/library/logger/load-packages-in-background-process.R
/usr/lib64/R/library/logger/tests/testthat.R
/usr/lib64/R/library/logger/tests/testthat/test-CRANSKIP-appenders.R
/usr/lib64/R/library/logger/tests/testthat/test-CRANSKIP-helpers.R
/usr/lib64/R/library/logger/tests/testthat/test-CRANSKIP-hooks.R
/usr/lib64/R/library/logger/tests/testthat/test-CRANSKIP-logger-namespaces.R
/usr/lib64/R/library/logger/tests/testthat/test-appender.R
/usr/lib64/R/library/logger/tests/testthat/test-eval.R
/usr/lib64/R/library/logger/tests/testthat/test-formatters.R
/usr/lib64/R/library/logger/tests/testthat/test-helpers.R
/usr/lib64/R/library/logger/tests/testthat/test-layout.R
/usr/lib64/R/library/logger/tests/testthat/test-logger.R
/usr/lib64/R/library/logger/tests/testthat/test-utils.R
