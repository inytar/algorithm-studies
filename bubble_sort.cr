# A naive bubble implementation in crystal. The loop will stop when no values are swapped anymore. crystal bubble_sort.cr will run the tests in this file.
class BubbleSort
  def self.call(a : Array) : Array
    while true
      swapped = false
      # Loop through the array from the second to the last value. Use the index to compare
      # the value with the previous one in the original array.
      a[1..-1].each_with_index do |v,i|
        # If the previous value in the orginal array is less than the the gotten value v, swap them.
        if a[i] > v
          # Swap the values.
          a[i+1] = a[i]
          a[i] = v
          # Set swapped to true, this will result in the main while loop
          # repeating it self.
          swapped = true
        end
        # Update the index to the next value.
        i = i + 1
      end
      # If we did not swap we are done, exit the main loop.
      if !swapped
        break
      end
    end
    # Return the sorted array.
    a
  end
end

# Tests.
class Test
  def call(bs)
    a = [2, 1, 3] of Int32

    if bs.call(a) != [1, 2, 3]
      raise "Sorting failed #{a}"
    end

    a = [3, 2, 1, -1] of Int32

    if bs.call(a) != [-1, 1, 2, 3]
      raise "Sorting failed #{a}"
    end

    a = [1, 2, 3] of Int32

    if bs.call(a) != [1, 2, 3]
      raise "Sorting failed #{a}"
    end

    a = [1.1, 1.0, 2.5]

    if bs.call(a) != [1.0, 1.1, 2.5]
      raise "Sorting failed #{a}"
    end

    a = [1.1, 1, 2.5]

    b = bs.call(a)
    if b != [1, 1.1, 2.5]
      raise "Sorting failed #{a}"
    end

    if !b[0].is_a?(Int32)
      raise "Types should not change"
    end

    # Test stability.

    a = [1, 1.0, 2.5]

    b = bs.call(a)
    if b != [1, 1.0, 2.5]
      raise "Sorting failed #{a}"
    end

    if !b[0].is_a?(Int32)
      raise "Not stable"
    end

    a = [1.0, 1, 2.5]

    b = bs.call(a)
    if b != [1.0, 1, 2.5]
      raise "Sorting failed #{a}"
    end

    if b[0].is_a?(Int32)
      raise "Not stable"
    end
  end
end

Test.call(BubbleSort)

# If objects in array are not comperable compiling fails.
