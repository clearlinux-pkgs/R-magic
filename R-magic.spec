#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-magic
Version  : 1.6.0
Release  : 47
URL      : https://cran.r-project.org/src/contrib/magic_1.6-0.tar.gz
Source0  : https://cran.r-project.org/src/contrib/magic_1.6-0.tar.gz
Summary  : Create and Investigate Magic Squares
Group    : Development/Tools
License  : GPL-2.0
Requires: R-abind
BuildRequires : R-abind
BuildRequires : buildreq-R

%description
analysis of arbitrarily dimensioned arrays.  The original motivation
 for the package was the development of efficient, vectorized
 algorithms for the creation and investigation of magic squares and
 high-dimensional magic hypercubes.

%prep
%setup -q -c -n magic
cd %{_builddir}/magic

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1644425857

%install
export SOURCE_DATE_EPOCH=1644425857
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
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library magic
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library magic
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library magic
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc magic || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/magic/CITATION
/usr/lib64/R/library/magic/DESCRIPTION
/usr/lib64/R/library/magic/INDEX
/usr/lib64/R/library/magic/Meta/Rd.rds
/usr/lib64/R/library/magic/Meta/data.rds
/usr/lib64/R/library/magic/Meta/features.rds
/usr/lib64/R/library/magic/Meta/hsearch.rds
/usr/lib64/R/library/magic/Meta/links.rds
/usr/lib64/R/library/magic/Meta/nsInfo.rds
/usr/lib64/R/library/magic/Meta/package.rds
/usr/lib64/R/library/magic/Meta/vignette.rds
/usr/lib64/R/library/magic/NAMESPACE
/usr/lib64/R/library/magic/NEWS.md
/usr/lib64/R/library/magic/R/magic
/usr/lib64/R/library/magic/R/magic.rdb
/usr/lib64/R/library/magic/R/magic.rdx
/usr/lib64/R/library/magic/data/Frankenstein.rda
/usr/lib64/R/library/magic/data/Ollerenshaw.rda
/usr/lib64/R/library/magic/data/cube2.rda
/usr/lib64/R/library/magic/data/hendricks.rda
/usr/lib64/R/library/magic/data/magiccubes.rda
/usr/lib64/R/library/magic/data/perfectcube5.rda
/usr/lib64/R/library/magic/data/perfectcube6.rda
/usr/lib64/R/library/magic/doc/index.html
/usr/lib64/R/library/magic/doc/magic.R
/usr/lib64/R/library/magic/doc/magic.Rnw
/usr/lib64/R/library/magic/doc/magic.pdf
/usr/lib64/R/library/magic/help/AnIndex
/usr/lib64/R/library/magic/help/aliases.rds
/usr/lib64/R/library/magic/help/figures/magic.png
/usr/lib64/R/library/magic/help/magic.rdb
/usr/lib64/R/library/magic/help/magic.rdx
/usr/lib64/R/library/magic/help/paths.rds
/usr/lib64/R/library/magic/html/00Index.html
/usr/lib64/R/library/magic/html/R.css
/usr/lib64/R/library/magic/magic_stickermaker.R
/usr/lib64/R/library/magic/tests/aaa.R
