{pkgs}: {
  deps = [
    pkgs.vim
    pkgs.python312Packages.conda
    pkgs.imagemagick_light
    pkgs.haskellPackages.PropLogic
  ];
}
