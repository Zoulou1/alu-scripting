#!/usr/bin/env ruby
# This script prints all occurrences of the word "School" from the argument

# Match the word "School" and print all occurrences
puts ARGV[0].scan(/School/).join
