FRUIT=$1
if [ "$FRUIT" = "APPLE" ]; then
    echo "You selected Apple"
elif [ "$FRUIT" = "BANANA" ]; then
    echo "You selected Banana"
elif [ "$FRUIT" = "GRAPE" ]; then
    echo "You selected Grape"
else
    echo "Unknown fruit"
fi