#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-magic
Version  : 1.5.9
Release  : 15
URL      : https://cran.r-project.org/src/contrib/magic_1.5-9.tar.gz
Source0  : https://cran.r-project.org/src/contrib/magic_1.5-9.tar.gz
Summary  : Create and Investigate Magic Squares
Group    : Development/Tools
License  : GPL-2.0
Requires: R-abind
BuildRequires : R-abind
BuildRequires : buildreq-R

%description
creation and investigation of magic squares and hypercubes, including
 a variety of functions for the manipulation and analysis of
 arbitrarily dimensioned arrays.  The package includes methods for
 creating normal magic squares of any order greater than 2.  The
 ultimate intention is for the package to be a computerized embodiment
 all magic square knowledge, including direct numerical verification
 of properties of magic squares (such as recent results on the
 determinant of odd-ordered semimagic squares).  Some antimagic
 functionality is included.  The package also
 serves as a rebuttal to the often-heard comment "I thought R
 was just for statistics".

%prep
%setup -q -c -n magic

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1537203219

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1537203219
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library magic
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library magic
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library magic
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library magic|| : 
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :


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
/usr/lib64/R/library/magic/doc/magicpaper.R
/usr/lib64/R/library/magic/doc/magicpaper.Rnw
/usr/lib64/R/library/magic/doc/magicpaper.pdf
/usr/lib64/R/library/magic/help/AnIndex
/usr/lib64/R/library/magic/help/aliases.rds
/usr/lib64/R/library/magic/help/magic.rdb
/usr/lib64/R/library/magic/help/magic.rdx
/usr/lib64/R/library/magic/help/paths.rds
/usr/lib64/R/library/magic/html/00Index.html
/usr/lib64/R/library/magic/html/R.css
