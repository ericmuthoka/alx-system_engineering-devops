#!/usr/bin/env ruby

input_string = ARGV[0]

input_string.scan(/School/) do |match|
  puts match
end
