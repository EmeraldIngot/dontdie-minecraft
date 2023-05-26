pyver=`python3 --version | cut -d ' ' -f 2`
if [[ $pyver == *.*.* ]]; then
        pyver=`echo $pyver | cut -f1,2 -d'.'`
fi
~/Library/Python/$pyver/bin/pyinstaller dontdie-macos.spec