sudo -ln

if [ $? -eq 1 ]; then
    echo "     Password required. If you know the password, don't forget to try (sudo -l) with the password."
fi