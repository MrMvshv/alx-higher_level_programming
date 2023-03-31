#!/bin/bash
# makes request causing server to respond You got me!
curl -sL -X PUT -H "Origin: School" -d "user_id=98" 84.72.72.228:5000/catch_me
