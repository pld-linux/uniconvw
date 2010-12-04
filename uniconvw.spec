Summary:	GTK+ frontend to Uniconvertor
Summary(pl.UTF-8):	Interfejs GTK+ do Uniconvertora
Name:		uniconvw
Version:	1.1.5
Release:	1
License:	LGPL v2+
Group:		Applications/Graphics
#Source0Download: http://code.google.com/p/uniconvertor/downloads/list
Source0:	http://uniconvertor.googlecode.com/files/%{name}-%{version}.tar.gz
# Source0-md5:	b36856662c26f9ded3580eab6a09d91f
URL:		http://sk1project.org/modules.php?name=Products&product=uniconvertor
BuildRequires:	python >= 1:2.5
BuildRequires:	python-modules >= 1:2.5
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
%pyrequires_eq	python
Requires:	python-pygtk-gtk >= 2:2.0
Requires:	python-sk1libs >= 0.9.1
Requires:	uniconvertor >= 1.1.5
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GTK+ frontend to Uniconvertor, vector graphics format converter.

%description -l pl.UTF-8
Interfejs GTK+ do Unicovertora - konwertera formatów grafiki
wektorowej.

%prep
%setup -q

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT

%{__python} setup.py install \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

# these files are used only on Windows
%{__rm} -r $RPM_BUILD_ROOT%{py_sitescriptdir}/uniconvw/uc_win
%{__rm} $RPM_BUILD_ROOT%{py_sitescriptdir}/uniconvw/resources/uniconvw_icon_16.ico
# packaged as doc/in common-licenses
%{__rm} $RPM_BUILD_ROOT%{py_sitescriptdir}/uniconvw/{COPYRIGHTS,GNU_GPL_v2,GNU_LGPL_v2}

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README src/COPYRIGHTS
%attr(755,root,root) %{_bindir}/uniconvw
%dir %{py_sitescriptdir}/uniconvw
%{py_sitescriptdir}/uniconvw/VERSION
%{py_sitescriptdir}/uniconvw/__init__.py[co]
%{py_sitescriptdir}/uniconvw/resources
%{py_sitescriptdir}/uniconvw/uc_gtk
%{py_sitescriptdir}/uniconvw-*.egg-info
%{_desktopdir}/uniconvw.desktop
%{_pixmapsdir}/uniconvw.png
%{_pixmapsdir}/uniconvw.xpm
