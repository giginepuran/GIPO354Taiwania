#!/bin/bash

cd ~
if [[ ! -d "~/bin" ]];then
    mkdir bin
    echo "Created directory ~/bin"
fi

git_username="giginepuran"
git_email="giginepuran@gmail.com"
git config --global user.name $git_username
git config --global user.email $git_email

#powerline  fonts
git clone https://github.com/powerline/fonts.git --depth=1
cd fonts
./install.sh
cd ..
rm -rf fonts

#zsh
#install to ~
cd ~
wget -O zsh.tar.gz https://sourceforge.net/projects/zsh/files/latest/download
mkdir zsh && tar -xvf zsh.tar.gz -C zsh --strip-components 1
cd zsh
./configure --prefix=$HOME
make
make install
rm ~/zsh.tar.gz
#oh-my-zsh
git clone https://github.com/robbyrussell/oh-my-zsh.git ~/.oh-my-zsh
cp ~/.oh-my-zsh/templates/zshrc.zsh-template ~/.zshrc
sed -i 's/^ZSH_THEME="robbyrussell"/ZSH_THEME="rkj-repos"/g' ~/.zshrc
# this is necessary for vim highlight in zsh
echo 'alias tmux="TERM=xterm-256color tmux"' >> ~/.zshrc

#chsh without root
#echo '# My setting' >> ~/.bash_profile
echo 'zsh' >> ~/.bash_profile


