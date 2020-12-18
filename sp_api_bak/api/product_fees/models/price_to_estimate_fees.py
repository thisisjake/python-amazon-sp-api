# coding: utf-8

"""
    Selling Partner API for Product Fees

    The Selling Partner API for Product Fees lets you programmatically retrieve estimated fees for a product. You can then account for those fees in your pricing.  # noqa: E501

    OpenAPI spec version: v0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class PriceToEstimateFees(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'listing_price': 'MoneyType',
        'shipping': 'MoneyType',
        'points': 'Points'
    }

    attribute_map = {
        'listing_price': 'ListingPrice',
        'shipping': 'Shipping',
        'points': 'Points'
    }

    def __init__(self, listing_price=None, shipping=None, points=None):  # noqa: E501
        """PriceToEstimateFees - a model defined in Swagger"""  # noqa: E501
        self._listing_price = None
        self._shipping = None
        self._points = None
        self.discriminator = None
        self.listing_price = listing_price
        if shipping is not None:
            self.shipping = shipping
        if points is not None:
            self.points = points

    @property
    def listing_price(self):
        """Gets the listing_price of this PriceToEstimateFees.  # noqa: E501


        :return: The listing_price of this PriceToEstimateFees.  # noqa: E501
        :rtype: MoneyType
        """
        return self._listing_price

    @listing_price.setter
    def listing_price(self, listing_price):
        """Sets the listing_price of this PriceToEstimateFees.


        :param listing_price: The listing_price of this PriceToEstimateFees.  # noqa: E501
        :type: MoneyType
        """
        if listing_price is None:
            raise ValueError("Invalid value for `listing_price`, must not be `None`")  # noqa: E501

        self._listing_price = listing_price

    @property
    def shipping(self):
        """Gets the shipping of this PriceToEstimateFees.  # noqa: E501


        :return: The shipping of this PriceToEstimateFees.  # noqa: E501
        :rtype: MoneyType
        """
        return self._shipping

    @shipping.setter
    def shipping(self, shipping):
        """Sets the shipping of this PriceToEstimateFees.


        :param shipping: The shipping of this PriceToEstimateFees.  # noqa: E501
        :type: MoneyType
        """

        self._shipping = shipping

    @property
    def points(self):
        """Gets the points of this PriceToEstimateFees.  # noqa: E501


        :return: The points of this PriceToEstimateFees.  # noqa: E501
        :rtype: Points
        """
        return self._points

    @points.setter
    def points(self, points):
        """Sets the points of this PriceToEstimateFees.


        :param points: The points of this PriceToEstimateFees.  # noqa: E501
        :type: Points
        """

        self._points = points

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(PriceToEstimateFees, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, PriceToEstimateFees):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other