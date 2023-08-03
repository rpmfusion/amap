Name:           amap
Version:        5.4
Release:        18%{?dist}
Summary:        Network tool for application protocol detection
License:        AMAP License
#License        AMAP non-commercial rules added to GPLv2
URL:            https://github.com/hackerschoice/THC-Archive
Source0:        https://github.com/hackerschoice/THC-Archive/raw/master/Tools/%{name}-%{version}.tar.gz
Patch0:         %{name}-destdir.patch
Patch1:         %{name}-path.patch
Patch2:         %{name}-ldflags.patch
Patch3:         %{name}-new-homepage.patch
Patch4:         %{name}-system-pcre.patch
Patch5:         %{name}-optflags.patch
Patch6:         %{name}-lnamap6.patch
Patch7:         %{name}-openssl.patch

BuildRequires:  gcc
BuildRequires:  openssl-devel
BuildRequires:  pcre-devel

%description
THC Amap is a next-generation tool for assisting network penetration testing.
It performs fast and reliable application protocol detection, independent
on the TCP/UDP port they are being bound to.

%prep
%setup -q
%patch0 -p1 -b .0destdir
%patch1 -p1 -b .1path
%patch2 -p1 -b .2ldflags
#%patch3 -p1 -b .3homepage
%patch4 -p1 -b .4pcre
%patch5 -p1 -b .5optflags
%patch6 -p1 -b .6lnamap6
%patch7 -p1 -b .openssl

%build
#%%configure
./configure --prefix=%{_prefix} --libdir=%{_libdir}
%{make_build} OPT="$RPM_OPT_FLAGS"


%install
%{make_install}

%files
%doc CHANGES README TODO
%license LICENCE.AMAP LICENSE.GNU
%{_bindir}/*
%{_mandir}/man1/%{name}.1*
%{_datadir}/%{name}/

%changelog
* Thu Aug 03 2023 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 5.4-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Aug 08 2022 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 5.4-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild and ffmpeg
  5.1

* Thu Feb 10 2022 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 5.4-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Aug 03 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 5.4-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Feb 04 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 5.4-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Aug 19 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 5.4-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Feb 05 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 5.4-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Aug 13 2019 Leigh Scott <leigh123linux@gmail.com> - 5.4-11
- Fix openssl not found on x86_64
- Remove BuildRoot tag
- Remove Group tag
- Remove clean section
- Remove defattr from files
- Spec file clean up
- Install license file correctly

* Sat Aug 10 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 5.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Mar 05 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 5.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Aug 19 2018 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 5.4-8
- Rebuilt for Fedora 29 Mass Rebuild binutils issue

* Fri Jul 27 2018 RPM Fusion Release Engineering <sergio@serjux.com> - 5.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Mar 02 2018 RPM Fusion Release Engineering <leigh123linux@googlemail.com> - 5.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 31 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 5.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Mar 25 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 5.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Sep 01 2014 Sérgio Basto <sergio@serjux.com> - 5.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri May 23 2014 Michal Ambroz <rebus at, seznam.cz> 5.4-2
- bump to version 5.4

* Wed Nov 21 2012 Nicolas Chauvet <kwizart@gmail.com> - 5.2-6
- Rebuilt

* Thu Feb 09 2012 Nicolas Chauvet <kwizart@gmail.com> - 5.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Mar 26 2010 Michal Ambroz <rebus at, seznam.cz> 5.2-4
- more flexible pcre cflags to build also on RHEL4

* Sun Mar 20 2010 Michal Ambroz <rebus at, seznam.cz> 5.2-3
- License changed to AMAP license to avoid confusion
- patch makefile to link to amap6 instead of copy


* Fri Jan 08 2010 Michal Ambroz <rebus at, seznam.cz> 5.2-2
- patched makefile & spec to honour RPM_OPT_FLAGS
- included verbatim copy of licenses
- RPM_OPT_FLAGS fixed build of debug package as well
- removed explicit dependency on openssl and pcre

* Tue Jan 05 2010 Michal Ambroz <rebus at, seznam.cz> 5.2-1
- Initial SPEC for Fedora 12 using SPEC and patches from PLD
- Original SPEC by luzik qboosh zbyniu baggins glen


