Summary:	IETF Opus Interactive Audio Codec
Name:		opus
Version:	1.0.1
Release:	1
License:	BSD
Group:		Libraries
Source0:	http://downloads.xiph.org/releases/opus/%{name}-%{version}.tar.gz
# Source0-md5:	bbac19996957b404a1139816e2f357f5
URL:		http://opus-codec.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Opus codec is designed for interactive speech and audio
transmission over the Internet. It is designed by the IETF Codec
Working Group and incorporates technology from Skype's SILK codec and
Xiph.Org's CELT codec.

%package devel
Summary:	Header files for OPUS libraries
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for OPUS libraries.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules	\
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /usr/sbin/ldconfig
%postun	-p /usr/sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING README
%attr(755,root,root) %ghost %{_libdir}/libopus.so.0
%attr(755,root,root) %{_libdir}/libopus.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libopus.so
%{_libdir}/libopus.la
%{_includedir}/opus
%{_pkgconfigdir}/opus.pc
%{_aclocaldir}/opus.m4

