{pkgs}: {
  deps = [
    pkgs.python312Packages.conda
    pkgs.imagemagick_light
    pkgs.haskellPackages.PropLogic
  ];
}
