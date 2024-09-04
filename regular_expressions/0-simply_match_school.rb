#!/usr/bin/env ruby
# This prints the word "school" if it is found in the argument

# The regular expression matches the word "School"
puts ARGV[0].scan(/School/).join
